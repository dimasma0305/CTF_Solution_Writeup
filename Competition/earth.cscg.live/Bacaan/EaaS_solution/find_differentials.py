#!/usr/bin/env pypy3
""" Finds differential characteristics for every S-box by brute-force. """

from collections import Counter

import des
import main  # changes the S-Box values in des

NUM_INPUT_VALUES = 64
NUM_OUTPUT_VALUES = 16
INPUT_VALUES = range(NUM_INPUT_VALUES)

for i, sbox in enumerate(des.core.SUBSTITUTION_BOX):
    stats = Counter()

    for input_difference in INPUT_VALUES:
        for input in INPUT_VALUES:
            output_difference = sbox[input] ^ sbox[input ^ input_difference]
            stats.update([(input_difference, output_difference)])

    print(f"\nSBOX[{i}]:\n")

    for (input_difference, output_difference), count in stats.most_common(5):
        probability = count / NUM_INPUT_VALUES
        print(
            f"    {input_difference:06b} -> {output_difference:04b} has probability {probability} (bias = {probability-1/NUM_OUTPUT_VALUES})"
        )
