class Solution:
    def recur_serve(self, soup_A, soup_B, service, dp, prob)-> float:
        if (soup_A, soup_B) in dp:
            return dp[(soup_A, soup_B)]
        if soup_A <= 0 and soup_B > 0:
            return 1
        elif soup_B <= 0 and  soup_A > 0 :
            return 0
        elif soup_A <= 0 and soup_B <= 0:
            return 0.5
        
        for i in service:            
            prob = prob + (0.25 * self.recur_serve(soup_A-i, soup_B-(100-i), service, dp, 0))
        dp[(soup_A, soup_B)] = prob

        return prob

    def soupServings(self, n: int) -> float:
        if n > 4451:
            return 1.0
        ser = [100, 75, 50, 25]
        mem = {}
        res = self.recur_serve(n, n, ser, mem, 0)
        return res

n = 800 
sol = Solution()
res = sol.soupServings(n)
print(res)

# To find 4451 use binary search