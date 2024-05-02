from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                last = stack.pop()
                ans[last] = i - last
            stack.append(i)
        return ans 
array = [89,62,70,58,47,47,46,76,100,70]
sol= Solution()
res = sol.dailyTemperatures(array)
print(res)