class Solution:
    def rec_path(self, x, y, row, col, sol)-> int:
        if x == row-1 and y == col-1:
            return sol+1

        if x < row-1:
            sol = self.rec_path(x+1, y, row, col, sol)
        
        if y < col-1:
            sol = self.rec_path(x, y+1, row, col, sol)
        
        return sol

    def uniquePaths(self, m: int, n: int) -> int:
        res = self.rec_path(0, 0, m, n, 0)
        return res

"""
//Second Solution
class Solution:
    def rec_fact(self, n)->int:
        if n == 0 or n == 1:
            return 1
        return n * self.rec_fact(n-1)

    def uniquePaths(self, m: int, n: int) -> int:
        tot_path = (m-1)+(n-1)
        tot_cell = self.rec_fact(tot_path)
        row_path = self.rec_fact(m-1)
        col_path = self.rec_fact(n-1)
        res = tot_cell//((row_path)*(col_path))

        return res
    
"""
    
row_test = 23
column_test = 12
test = Solution()
output = test.uniquePaths(row_test, column_test)
print(output)