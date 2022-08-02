# Solution: Encryption as a Service

## Challenge

We get the code for a service that 
-  generates a random key k
-  reads a plaintext from the user 
-  encrypts it using a variant of DES with custom values for three of the S-Boxes
-  sends us the ciphertext and the flag encrypted using the same key

While the flag is encrypted in CBC mode the user plaintext is encrypted in EBC mode.
This allows us to freely chose many plaintext blocks Pᵢ and retrieve DESₖ(Pᵢ).

## Helpful resources:

To solve (and build) the challenge I had to use the following resources:

- [An description of the DES algorithm](https://en.wikipedia.org/wiki/Data_Encryption_Standard#Description)
- [The DES implementation used in the challenge](https://github.com/0x10001/des)
- [This tutorial on differential cryptanalysis](https://www.engr.mun.ca/~howard/PAPERS/ldc_tutorial.pdf)

## Deciding on an cryptanalysis technique.

The key can be recovered by differential cryptanalysis. The idea to test the S-boxes for
differential characteristics can be found by reading the Wikipedia entry for DES or by 
testing different attacks from a list of [standard attacks](https://en.wikipedia.org/wiki/Block_cipher#Cryptanalysis) on block ciphers.

I think it should be a fairly obvious first step to write a script that outputs possible differential characteristics
and linear approximations and then decide to use differential cryptanalysis, but I might write a hint to use
differential cryptanalysis in the description.

## Finding differentials

`./find_differentials.py` finds high probability differential characteristics in the S-boxes
by just counting the output differences for every possible pair of inputs for every S-Box.

Output (edited):
```
SBOX[2]: 000100 -> 0010 has probability 0.75 (bias = 0.6875)
SBOX[3]: 000010 -> 0010 has probability 0.75 (bias = 0.6875)
SBOX[7]: 000100 -> 0010 has probability 0.75 (bias = 0.6875)
```

`./combine_differentials.py` calculates a round function differential to each of the three 
S-box differentials above, and then for every combination of these differentials 
calculates the corresponding differential for the whole cipher.

From the output we select the following line, because it involves 3 active S-boxes in both
the first and last round of the cipher. 
```
0020020000003000 -> 0030030000002000 has theoretical probability 0.0008 and empirical probability 0.0007 - 36 active key bits.
```
This way we need only one differential for the next step.

## Extracting key bits

We use the differential Δ → Δ' selected in the previous step, generate 10⁵ random blocks Pᵢ
and for every Pᵢ send Pᵢ and Pᵢ⊕Δ to the service.

If for a given Pᵢ the differential holds (DESₖ(Pᵢ)⊕ DESₖ(Pᵢ⊕ Δ) = Δ') than we can assume that 
the differentials of the first and last round hold too.

We call the pairs (Pᵢ, Pᵢ⊕Δ) for which the differential holds "right pairs" and ignore the other pairs.

The probability for a right pair to be right "by chance" and not due to the differentials for every round
holding is about 2⁻⁶⁴/0.0008 ≈ 6.776·10¹⁷.

We can extract 36 bits from the round keys using the following observations:
- In Feistel ciphers we know the input to the round function for the first and the last round.
- Every S-Box is influenced by only 6 bits of the round key.
- Because the differential for the round holds the differential for each of the active S-boxes holds too.

For every active S-box we can extract 6 bits of the round key:
If for a given input and a guess for a partial key (the 6 bits influencing the S-box) the
S-box differential does not hold we can rule out the partial key.
If we do this for every right pair only one partial key remains.

`./solve.py` uses this to extract 28 key bits of the user key.
We do not get 36 key bits, because the 18 bits we extract from the first round key and those
from the last round key overlap when mapped to the user key.

`./solve.py` then brute-forces the remaining 28 key bits to get the flag.

The brute-force part takes about 25 minutes to search the entire keyspace on my machine 
using PyPy and about 10x longer using CPython.
