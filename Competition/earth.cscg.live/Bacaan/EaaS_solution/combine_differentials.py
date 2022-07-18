#!/usr/bin/env pypy3

""" Combines the S-box differentials from the previous step into differentials 
for the F-function and then for the whole cipher.
"""

from collections import Counter, namedtuple
from random import randrange

from itertools import product

import des.core as des
from more_itertools import powerset

import main  # changes the SBox values


def randbytes(n):
    """ Replacement for random.randbytes, which does not work with PyPy. """
    return randrange(0, 2 ** (8 * n)).to_bytes(n, "big")


SboxDifferential = namedtuple(
    "SboxDifferential", "sbox input_difference output_difference probability"
)
Differential = namedtuple(
    "Differential", "input_difference output_difference probability"
)


def xor(differentials):
    """ Combine two differentials in different S-boxes into a new differential. """
    input_difference = output_difference = 0
    probability = 1

    for d in differentials:
        input_difference ^= d.input_difference
        output_difference ^= d.output_difference
        probability *= d.probability

    return Differential(input_difference, output_difference, probability)


def random_round_key():
    return randrange(0, 2**48)


# Differentials for the SBoxes from find_differentials.py
sbox_differentials = (
    SboxDifferential(2, 0b000100, 0b0010, 0.75),
    SboxDifferential(3, 0b000010, 0b0010, 0.75),
    SboxDifferential(7, 0b000100, 0b0010, 0.75),
)


def get_f_differential(sbox_differential):
    """Find the corresponding differentials of the function F (round function)."""

    assert (
        sbox_differential.input_difference & 0b000110
        == sbox_differential.input_difference
    )

    input_difference = sbox_differential.input_difference << (
        (7 - sbox_differential.sbox) * 4
    )
    output_difference = sbox_differential.output_difference << (
        (7 - sbox_differential.sbox) * 4
    )
    output_difference = des.permute(output_difference, 32, des.PERMUTATION)

    return Differential(
        input_difference, output_difference, sbox_differential.probability
    )


f_differentials = list(map(get_f_differential, sbox_differentials))

# XOR sums of differentials are differentials too.
f_differentials = [xor(diff_set) for diff_set in powerset(f_differentials)]


def get_active_key_bits(difference):
    """
    Given an input or output difference calculate the active key bits for
    the first or last round respectively.
    """

    diff = des.permute(difference, 64, des.INITIAL_PERMUTATION)
    diff &= 0xffffffff
    diff = des.permute(diff, 32, des.EXPANSION)

    active_key_bits = 0
    for i in range(len(des.SUBSTITUTION_BOX)):
        mask = 0b111111 << i * 6
        if diff & mask != 0:
            active_key_bits |= mask

    return active_key_bits


def verify_differential(
    differential: Differential,
    bits: int,
    function,
    count_active_key_bits=False,
    iters=10**5,
):
    counter = Counter()
    in_diff = differential.input_difference
    out_diff = differential.output_difference

    for _ in range(iters):
        in_block = randrange(0, 2**bits)
        out_block_diff = function(in_block) ^ function(in_block ^ in_diff)
        counter.update([out_block_diff])

    assert out_diff == counter.most_common()[0][0]
    occurences = counter.most_common()[0][1]

    # Count number of active key bits in first and last round
    # The actual number of active bits in the user key might be lower, because 
    # the corresponding bits in the user key for the round keys might overlap.
    active_key_bits = bin(get_active_key_bits(in_diff)).count("1")
    active_key_bits += bin(get_active_key_bits(out_diff)).count("1")

    print(
        f"    {in_diff:0{bits//4}x} -> {out_diff:0{bits//4}x} has theoretical probability {diff.probability:6.4f} and empirical probability {occurences/iters:6.4f}",
        end="",
    )
    print(f" - {active_key_bits:2} active key bits." if count_active_key_bits else "")
    # print(f"    {differential.input_difference:0{bits//4}x} -> {differential.output_difference:0{bits//4}x} has theoretical probability {differential.probability:6.4f} and empirical probability {occurences/iters}")


print("\nF-function differentials:\n")
for diff in f_differentials:
    key = random_round_key()
    verify_differential(diff, 32, lambda block: des.f(block, key))


def get_des_differential(left_difference, right_difference):
    """Find a differential for the whole cipher given differences for L₀ and R₀."""

    probability = 1

    # Calculate back to the DES input.
    input_difference = left_difference << 32 | right_difference
    input_difference = des.permute(input_difference, 64, des.INVERSE_PERMUTATION)

    # Calculate forward to the DES output.
    for _ in range(16):

        # Find matching differential to approximate F.
        differential = next(
            d for d in f_differentials if d.input_difference == right_difference
        )

        probability *= differential.probability
        left_difference, right_difference = (
            right_difference,
            left_difference ^ differential.output_difference,
        )

    output_difference = right_difference << 32 | left_difference
    output_difference = des.permute(output_difference, 64, des.INVERSE_PERMUTATION)

    return Differential(input_difference, output_difference, probability)


# Get DES differential for every combination of left and right differential.
differentials = [
    get_des_differential(left.input_difference, right.input_difference)
    for left, right in product(f_differentials, repeat=2)
]

differentials.sort(reverse=True, key=lambda d: d.probability)

print("\nWhole cipher differentials:\n")
for diff in differentials:
    key = list(des.derive_keys(randbytes(8)))
    verify_differential(
        diff,
        64,
        lambda block: des.encode_block(block, key, True),
        count_active_key_bits=True,
    )
