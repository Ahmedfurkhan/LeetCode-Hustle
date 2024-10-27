class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        This function counts the number of all the 1's squares present 
        in a given 2D binary matrix.

        Args:
        matrix (List[List[int]]): A 2D binary matrix where 1's represent 
        filled cells and 0's represent empty cells.

        Returns:
        int: The total count of 1's squares present in the matrix.
        """

        # Get dimensions of the matrix
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        # Create a DP table with same dimensions as matrix
        dp_table = [[0] * n_cols for _ in range(n_rows)]

        # Initialize total count of squares
        total_count = 0

        # Initialize first row and column of DP table
        for i in range(n_rows):
            dp_table[i][0] = matrix[i][0]
            total_count += dp_table[i][0]
        for j in range(1, n_cols):
            dp_table[0][j] = matrix[0][j]
            total_count += dp_table[0][j]

        # Fill the DP table for remaining cells
        for i in range(1, n_rows):
            for j in range(1, n_cols):
                if matrix[i][j] == 1:
                    # Find minimum of left, top, and diagonal cells and add 1
                    dp_table[i][j] = 1 + min(dp_table[i-1][j-1], 
                                             dp_table[i-1][j], 
                                             dp_table[i][j-1])
                total_count += dp_table[i][j]

        return total_count