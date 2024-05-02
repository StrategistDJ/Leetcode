from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        l = len(nums)
        pos = 0

        for i in range(l):
            if nums[i] != 0:    
                slow = i
                fast = (nums[i] + i)%l

                while nums[slow]*nums[fast] > 0 and nums[slow] * nums[(nums[fast]+fast)%l] > 0:
                    if slow == fast:
                        if slow != (nums[slow]+slow)%l:
                            return True
                        else:
                            break
                    slow = (nums[slow]+slow)%l
                    fast = (nums[(nums[fast]+ fast)%l] + (nums[fast]+ fast)%l)%l
                
                j = i
                while nums[j] * nums[(nums[j]+j)%l]>0:
                    nums[j] = 0
                    j = (nums[j]+j)%l
        
        return False

    
sample = [1,-1,5,1,4]
sol = Solution()
res = sol.circularArrayLoop(sample)
print(res)