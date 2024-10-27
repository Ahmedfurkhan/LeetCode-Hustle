class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = 0

        for length in range(1, min(n, m) + 1):
            for i in range(n - length + 1):
                for j in range(m - length + 1):
                    if self.is_square(matrix, i, j, length):
                        res += 1

        return res

    def is_square(self, matrix, x, y, length):
        for i in range(x, x + length):
            for j in range(y, y + length):
                if matrix[i][j] != 1:
                    return False

        return True