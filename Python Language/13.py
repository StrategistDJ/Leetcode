'''
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}
        tot = 0
        i = 0
        while i < len(s):
            if i+1 < len(s):  
                if dict[s[i]] >= dict[s[i+1]]:
                    tot = tot + dict[s[i]]
                    i = i+1
                else:
                    tot = tot + (dict[s[i+1]]-dict[s[i]])
                    i = i+2
            else:
                tot = tot + dict[s[i]]
                i = i+1
        return tot
'''
# Second Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}
        tot = 0
        sum = 1000
        for i in range(len(s)):
            if sum >= dict[s[i]]:
                tot = tot + dict[s[i]]
                sum = dict[s[i]]
            else:
                tot = tot + (dict[s[i]]-sum) - sum
        return tot

sample = "MCMXCIV"
sol = Solution()
res = sol.romanToInt(sample)
print(res)