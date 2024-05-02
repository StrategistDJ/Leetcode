from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        sol = 0
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == target:
                    return sum
                
                if (abs(sum-target)) < min_diff:
                    min_diff = abs(sum-target)
                    sol = sum
                
                if sum < target:
                    j+=1
                else:
                    k-=1
        
        return sol
    
array = [0, 1, 2]
sample = 0
sol = Solution()
res = sol.threeSumClosest(array, sample)
print(res)