#!/usr/bin/env pypy3

import os

import des  # https://pypi.org/project/des/

from secret import FLAG

# Use custom sbox values.
des.core.SUBSTITUTION_BOX = list(des.core.SUBSTITUTION_BOX)

des.core.SUBSTITUTION_BOX[2] = (
     5,  8, 13,  6,  7,  2, 15,  4, 11, 14,  0,  3,  9, 12, 10,  1,
     3,  2, 15, 11,  1,  0, 12,  9, 13,  6,  7,  8, 14,  4,  5, 10,
     0, 15,  7, 14,  2,  9,  5, 12,  4, 11, 10,  1,  6, 13,  8,  3,
    12,  6,  1,  5, 14,  4,  3,  7,  0,  8, 15, 10,  2, 11, 13,  9,
)

des.core.SUBSTITUTION_BOX[3] = (
     4, 13,  6, 10, 12,  0, 14,  2, 15,  9,  8, 11,  5,  1,  7,  3,
     7,  9, 10, 11,  0, 14,  2, 12, 13,  4, 15,  6,  3,  5,  1,  8,
    10,  5,  0,  7,  6,  9,  4, 11,  8, 14,  2, 12,  1, 13,  3, 15,
     5,  3,  7,  1, 10,  6,  8,  4,  9, 15, 11,  0,  2, 14, 13, 12,
)

des.core.SUBSTITUTION_BOX[7] = (
     8,  0, 15,  7, 12,  2, 13,  5,  3, 10, 11,  6,  1, 14,  9,  4,
    11, 12,  3,  5,  9, 14,  1, 13,  7,  0,  4,  8, 15,  2,  6, 10,
     7,  9, 10,  0,  5, 11,  8, 14,  1,  4, 13,  2,  3,  6, 15, 12,
     9,  4,  8,  3,  1,  6, 10, 11,  0, 14,  5, 13,  2, 12,  7, 15,
)

key = des.DesKey(os.urandom(8))


def encrypt(plaintext, iv=None):
    ciphertext = key.encrypt(plaintext, padding=True, initial=iv)

    if iv is not None:
        return iv.hex() + ciphertext.hex()
    else:
        return ciphertext.hex()


def main():
    print("Welcome to the Data Encryption Service.")

    try:
        plaintext = bytes.fromhex(input("Enter some plaintext (hex): "))
    except ValueError:
        print("Please enter a hex string next time.")
        exit(0)
     
    print("Ciphertext:", encrypt(plaintext))
    print("Flag:", encrypt(FLAG.encode("ascii"), iv=os.urandom(8)))


if __name__ == "__main__":
    main()
