from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tmp = []
        k = 0
        j = 0
        for i in range(m+n):
            if j<m and k <n:
                if nums1[j] <= nums2[k] and j<m:
                    tmp.append(nums1[j])
                    j+=1
                else:
                    tmp.append(nums2[k])
                    k+=1
            elif j<m:
                tmp.append(nums1[j])
                j+=1
            elif k<n:
                tmp.append(nums2[k])
                k+=1
        if len(tmp)>0:
            for i in range(m+n):
                nums1[i] = tmp[i]

l1=[1,2,3,0,0,0]
l2=[2,5,6]
n1=3
n2=3

sol = Solution()
sol.merge(l1, n1, l2, n2)

for i in range(n1+n2):
    print(l1[i], end=" ")