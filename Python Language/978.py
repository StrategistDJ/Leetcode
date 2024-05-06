from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        count = 1
        mx = 0
        curr = 1
        check_1 = True
        check_2 = True
        if n == 1:
            return 1
        
        while curr < n:
            if check_1 and arr[curr-1] > arr[curr]:
                count+=1
                check_1 = False
                check_2 = True
                curr+=1
            elif check_2 and arr[curr-1] < arr[curr]:
                count+=1
                check_2 = False
                check_1 = True
                curr+=1
            else:
                if arr[curr-1] == arr[curr]:
                    curr+=1
                mx = max(mx, count)
                count = 1
                check_1 = True
                check_2 = True
        mx = max(mx,count)
        return mx

vec = [0,8,45,88,48,68,28,55,17,24]

sol = Solution()
res = sol.maxTurbulenceSize(vec)
print(res)