from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n= len(nums)
        s=set(nums[0:k+1])
        start = 0
        
        if len(s) < k+1:
            if len(s)!=n:
                return True
            else:
                return False
        for i in range(k+1, n):
            s.remove(nums[start])
            start+=1
            s.add(nums[i])
            if len(s) < k+1:
                return True
            
        return False

vec = [1,2,3,1,2,3]
size_wind = 2

sol = Solution()
res = sol.containsNearbyDuplicate(vec, size_wind)
print(res)