from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_num = sum(nums)

        return (n*(n+1)//2)-sum_num

array = [9,6,4,2,3,5,7,0,1]

sol = Solution()
res = sol.missingNumber(array)
print(res)