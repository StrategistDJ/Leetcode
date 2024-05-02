class Solution:
    def recur_comb(self, n, sol) -> int:
        if sol[n] != -1:
            return sol[n]
        tot = 0
        for i in range(n):
            tot += (self.recur_comb(n-i-1, sol) * self.recur_comb(i, sol))
        sol[n] = tot
        return tot

    def numTrees(self, n: int) -> int:
        sol = [-1]*(n+1)
        sol[0] = 1
        ans = self.recur_comb(n, sol)
        return ans

sample = 3
sol = Solution()
res = sol.numTrees(sample)
print(res)