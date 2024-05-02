import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        
        count = 2
        l = [1]*n
        l[0] = l[1] = 0

        for i in range(2,math.isqrt(n)+1):
            if l[i] == 1:
                for j in range(i*i, n, i):
                    if l[j] == 1:
                        count +=1
                    l[j] = 0
        return n - count 

            
    
sample = 10
sol = Solution()
res = sol.countPrimes(sample)
print(res)