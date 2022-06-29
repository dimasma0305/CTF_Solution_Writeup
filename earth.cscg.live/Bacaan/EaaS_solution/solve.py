#!/usr/bin/env pypy3

from collections import Counter, namedtuple
from random import randrange
from typing import Generator, Iterable, List, Tuple

import des.core as des
from des import DesKey
from pwn import *

import main  # changes the S-Box values in des


def interact(plaintext: Iterable[bytes]) -> Tuple[bytes, bytes]:
    if not args.HOST:
        io = process(["./main.py"])
    else:
        io = remote(args.HOST, args.PORT or 31337, ssl=True)

    with io:
        io.sendline(plaintext.hex().encode())

        io.readuntil(b"Ciphertext: ")
        ciphertext = bytes.fromhex(io.readlineS())

        io.readuntil(b"Flag: ")
        flag = bytes.fromhex(io.readlineS())

    return ciphertext, flag


def decrypt_flag(flag: bytes, key: DesKey) -> bytes:
    iv = flag[:8]
    ciphertext = flag[8:]
    return key.decrypt(ciphertext, initial=iv)


Pair = namedtuple("Pair", "plaintext1 ciphertext1 plaintext2 ciphertext2")
Differential = namedtuple("Differential", "input_difference output_difference")

BLOCKSIZE = 64
BYTES_PER_BLOCK = BLOCKSIZE // 8

# The differential for the whole cipher from combine_differentials.py
DIFFERENTIAL = Differential(0x0020020000003000, 0x0030030000002000)

# The S-Box differentials from find_differentials.py
SBOX_DIFFERENTIALS = {
    2: Differential(0b000100, 0b0010),
    3: Differential(0b000010, 0b0010),
    7: Differential(0b000100, 0b0010),
}

NUM_PAIRS = 10**5  # Expected number of right pairs = P(DIFFERENTIAL) * NUM_PAIRS = 80


def to_bytes(block: int) -> bytes:
    return block.to_bytes(BYTES_PER_BLOCK, "big")


def from_bytes(block: bytes) -> bytes:
    return int.from_bytes(block, "big")


def get_plaintext() -> Generator[bytes, None, None]:
    for _ in range(NUM_PAIRS):
        rand_block = randrange(0, 2**BLOCKSIZE)
        yield to_bytes(rand_block)
        yield to_bytes(rand_block ^ DIFFERENTIAL.input_difference)


def parse_pairs(plaintext, ciphertext) -> Generator[Pair, None, None]:
    assert len(plaintext) + BYTES_PER_BLOCK == len(ciphertext)
    assert len(plaintext) % (2 * BYTES_PER_BLOCK) == 0

    for i in range(0, len(plaintext), 2 * BYTES_PER_BLOCK):
        yield Pair(
            from_bytes(plaintext[i : i + BYTES_PER_BLOCK]),
            from_bytes(ciphertext[i : i + BYTES_PER_BLOCK]),
            from_bytes(plaintext[i + BYTES_PER_BLOCK : i + 2 * BYTES_PER_BLOCK]),
            from_bytes(ciphertext[i + BYTES_PER_BLOCK : i + 2 * BYTES_PER_BLOCK]),
        )


def filter_right_pairs(pairs: Iterable[Pair]) -> Generator[Pair, None, None]:
    for pair in pairs:
        if (
            DIFFERENTIAL.input_difference == pair.plaintext1 ^ pair.plaintext2
            and DIFFERENTIAL.output_difference == pair.ciphertext1 ^ pair.ciphertext2
        ):
            yield pair


def get_sbox_input(block: int, sbox_nr: int, partial_key: int) -> int:
    block = des.permute(block, 64, des.INITIAL_PERMUTATION)
    block = block & 0xFFFFFFFF  # if round_nr == 0 else block >> 32
    block = des.permute(block, 32, des.EXPANSION) ^ partial_key

    i6 = block >> 42 - sbox_nr * 6 & 0x3F
    return i6 & 0x20 | (i6 & 0x01) << 4 | (i6 & 0x1E) >> 1


def extract_key_bits(right_pairs: Iterable[Pair], sbox_nr: int, round_nr: int):
    partial_key_candidates = [k << 42 - sbox_nr * 6 for k in range(2**6)]

    stats = Counter()

    sbox = des.SUBSTITUTION_BOX[sbox_nr]
    sbox_differential = SBOX_DIFFERENTIALS[sbox_nr]

    for pair in right_pairs:
        assert pair.plaintext1 ^ pair.plaintext2 == DIFFERENTIAL.input_difference
        assert pair.ciphertext1 ^ pair.ciphertext2 == DIFFERENTIAL.output_difference

        assert round_nr in {
            0,
            15,
        }, "We only know the input to the f function for the first and last round."

        blocks = (
            (pair.plaintext1, pair.plaintext2)
            if round_nr == 0
            else (pair.ciphertext1, pair.ciphertext2)
        )

        for partial_key in partial_key_candidates:
            sbox_inputs = [
                get_sbox_input(block, sbox_nr, partial_key) for block in blocks
            ]

            assert sbox_inputs[0] ^ sbox_inputs[1] == sbox_differential.input_difference

            sbox_outputs = [sbox[input] for input in sbox_inputs]

            if sbox_outputs[0] ^ sbox_outputs[1] == sbox_differential.output_difference:
                stats.update([partial_key])

    results = stats.most_common(3)

    assert (
        results[0][1] == results[1][1] != results[2][1]
    )  # Two partial keys seem to be successful for all of the right pairs.

    partial_key1, partial_key2 = results[0][0], results[1][0]

    # We know the bits for which both keys agree. 
    partial_key = partial_key1 & partial_key2
    known_bits = 0b111111 << 42 - sbox_nr * 6
    known_bits ^= partial_key1 ^ partial_key2

    return partial_key, known_bits


def inverse_permute(data: int, bits: int, mapper: Tuple[int]):
    """ Inverse function of `des.permute`.

    Some of the permutation boxes are not invertible.
    Bits that can not be calculated are set to zero.
    """
    ret = 0
    for i, v in enumerate(mapper):
        if data & 1 << len(mapper) - 1 - i:
            ret |= 1 << bits - 1 - v

    return ret


def roundkey_to_user_key(key: int, round_nr: int) -> int:
    """ Calculates the user key from a round key.

    This is more or less the inverse function of `des.derived_keys`.

    User key bits that dont map to bits in the round key are set to zero.
    """

    key = inverse_permute(key, 56, des.PERMUTED_CHOICE2)
    key = key >> 28, key & (1 << 28) - 1

    for bits in des.ROTATES[round_nr::-1]:
        key = [des.rotate_left(k, 28 - bits) for k in key]

    key = key[0] << 28 | key[1]
    key = inverse_permute(key, 64, des.PERMUTED_CHOICE1)

    return key


plaintext = b"".join(get_plaintext())
ciphertext, flag = interact(plaintext)
right_pairs = list(filter_right_pairs(parse_pairs(plaintext, ciphertext)))

info(f"Found {len(right_pairs)} right pairs.")

partial_key = 0
known_bits = 0

# "Parity" bits are ignored so we can set them to zero.
for i in range(0, 64, 8):
    known_bits |= 1 << i

for round_nr in (0, 15):
    for sbox_nr in SBOX_DIFFERENTIALS:
        new_partial_key, new_known_bits = extract_key_bits(
            right_pairs, sbox_nr, round_nr
        )
        partial_key |= roundkey_to_user_key(new_partial_key, round_nr)
        known_bits |= roundkey_to_user_key(new_known_bits, round_nr)

unknown_bit_indices = [i for i in range(64) if 1 << i & known_bits == 0]

info(f"Partial key: {partial_key:064b}")
info(f"Known bits:  {known_bits:064b}")
info(f"Need to brute-force {len(unknown_bit_indices)} bits")

plaintext = right_pairs[0].plaintext1
ciphertext = right_pairs[0].ciphertext1


def check_key(unknown_bits: str):
    key = partial_key

    for index, bit in zip(unknown_bit_indices, unknown_bits):
        if bit == "1":
            key |= 1 << index

    derived_keys = des.derive_keys(key.to_bytes(8, "big"))

    return ciphertext == des.encode_block(plaintext, derived_keys, True)


missing_bits = iters.mbruteforce(check_key, "01", len(unknown_bit_indices), "fixed")

key = partial_key

for index, bit in zip(unknown_bit_indices, missing_bits):
    if bit == "1":
        key |= 1 << index

key = DesKey(key.to_bytes(8, "big"))
flag = decrypt_flag(flag, key).decode("ascii")
success(f"The flag is {flag}")
