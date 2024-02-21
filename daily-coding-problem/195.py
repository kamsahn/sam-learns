"""
Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
[2, 6, 9, 14, 22, 25],
[3, 8, 10, 15, 25, 30],
[10, 11, 12, 23, 30, 35],
[20, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.
"""


def smaller_and_larger(matrix: list[list[int]],
                       i1: int,
                       j1: int,
                       i2: int,
                       j2: int,) -> int:
    ans = 0
    length = len(matrix[0])
    lower = matrix[i1][j1]
    higher = matrix[i2][j2]
    
    for i in range(len(matrix)):
        for j in range(length):
            if matrix[i][j] < lower:
                ans += 1
            elif matrix[i][j] > higher:
                ans += length - j
                # add the rest of the line, since they are all greater than higher
                break
            elif lower < matrix[i][length-1] < higher:
                # the rest of the line is in between the targets
                break
    
    return ans


if __name__ == "__main__":
    m = [[1, 3, 7, 10, 15, 20],
         [2, 6, 9, 14, 22, 25],
         [3, 8, 10, 15, 25, 30],
         [10, 11, 12, 23, 30, 35],
         [20, 25, 30, 35, 40, 45]]
    i1 = 1
    j1 = 1
    i2 = 3
    j2 = 3
    
    print(smaller_and_larger(m, i1, j1, i2, j2))
    
"""kotlin
    fun main() {
    fun smallerAndLarger(matrix: List<List<Int>>,
                        i1: Int,
                        j1: Int,
                        i2: Int,
                        j2: Int): Int {
        var ans = 0
        val height = matrix.size
        val length = matrix[0].size
        val lower = matrix[i1][j1]
        val higher = matrix[i2][j2]

        for (i in (0..height-1)) {
            for (j in (0..length-1)) {
                if (matrix[i][j] < lower) {
                    ans += 1
                } else if (matrix[i][j] > higher) {
                    ans += length - j
                    break
                } else if (lower < matrix[i][length-1] && matrix[i][length-1] < higher) {
                    break
                }
            }
        }

        return ans
    }

    val m = listOf(
        listOf(1, 3, 7, 10, 15, 20),
        listOf(2, 6, 9, 14, 22, 25),
        listOf(3, 8, 10, 15, 25, 30),
        listOf(10, 11, 12, 23, 30, 35),
        listOf(20, 25, 30, 35, 40, 45)
    )
    val i1 = 1
    val j1 = 1
    val i2 = 3
    val j2 = 3
    println(smallerAndLarger(m, i1, j1, i2, j2))
}
"""
    
    
    
    