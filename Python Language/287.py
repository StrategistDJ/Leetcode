from typing import List

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        max_index=0
        for i in nums:
            if i > max_index:
                max_index = i
        
        tmp = [0]*(max_index+1)
        for i in nums:
            tmp[i]+=1
            if tmp[i]>1:
                return i
"""
#Second Solution using the linked list checking if there is a cycle or not
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

l = [1,3,4,2,2]
sol = Solution()
res = sol.findDuplicate(l)
for i in range(len(l)):
    print(l[i], end= "")