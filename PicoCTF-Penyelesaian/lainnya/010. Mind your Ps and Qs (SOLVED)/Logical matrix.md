# Logical matrix
A logical matrix, binary matrix, relation matrix, Boolean matrix, or (0,1) matrix is a matrix with entries from the Boolean domain B = {0, 1}. Such a matrix can be used to represent a binary relation between a pair of finite sets.
## Matrix representation of a relation
If R is a binary relation between the finite indexed sets X and Y (so R ⊆ X×Y), then R can be represented by the logical matrix M whose row and column indices index the elements of X and Y, respectively, such that the entries of M are defined by:
![M_{i,j}={\begin{cases}1&(x_{i},y_{j})\in R\\0&(x_{i},y_{j})\not \in R\end{cases}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/eef478cb5b173407069ff788941180e39d681fc8)
### Example
The binary relation R on the set {1, 2, 3, 4} is defined so that aRb holds if and only if a divides b evenly, with no remainder. For example, 2R4 holds because 2 divides 4 without leaving a remainder, but 3R4 does not hold because when 3 divides 4 there is a remainder of 1. The following set is the set of pairs for which the relation R holds.
{(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 3), (4, 4)}.
The corresponding representation as a logical matrix is:
![{\displaystyle {\begin{pmatrix}1&1&1&1\\0&1&0&1\\0&0&1&0\\0&0&0&1\end{pmatrix}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2385340e48921480e304eee226b5c0f566df63e0)
which includes a diagonal of ones since each number divides itself.

## Sumber
https://en.wikipedia.org/wiki/Logical_matrix