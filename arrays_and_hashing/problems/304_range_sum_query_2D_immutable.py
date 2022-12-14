# Given a 2D matrix matrix, handle multiple queries of the following type:
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Implement the NumMatrix class:
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# You must design an algorithm where sumRegion works on O(1) time complexity.

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        
        self.pSum = [[0] * (cols + 1) for r in range(rows + 1)]
        
        for r in range(1, rows + 1):
            prefix = 0
            for c in range(1, cols + 1):
                prefix += matrix[r-1][c-1]
                above = self.pSum[r-1][c]
                self.pSum[r][c] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        pfix = self.pSum[row2][col2]
        left = self.pSum[row2][col1-1]
        above = self.pSum[row1-1][col2]
        topLeft = self.pSum[row1-1][col1-1]
        
        return pfix - left - above + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)