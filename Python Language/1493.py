from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        mx = 0
        count_1 = 0
        count_2 = 0
        n = len(nums)
        p_zero = 0
        for i in range(n):
            if nums[i] == 0 and i > 0:
                count_2 = count_2 + count_1
                mx = max(mx,count_2)
                start = p_zero+1
                p_zero = i
                count_2 = count_1
                count_1 = 0
            else:
                if nums[i]!=0:
                    count_1+=1
        if mx == n:
            mx-=1
        
        return mx
    
vec = [1,1,0,1]

sol = Solution()
res = sol.longestSubarray(vec)
print(res)