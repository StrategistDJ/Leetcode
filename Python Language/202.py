class Solution:
    def isHappy(self, n: int) -> bool:
        find = False
        num_list=[]
        res = 0
        while not find and n not in num_list:
            res = 0
            while n != 0 :
                res = res + (n%10)*(n%10)
                n = n//10
            
            if res < 10 and res%2 == 0:
                num_list.append(res)

            if res == 1:
                find = True
            else:
                n = res

        return find

n = 4
  
sol = Solution()
res = sol.isHappy(n)
print(res)