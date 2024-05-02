class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        sub=""
        for c in range(len(haystack)):
            sub = haystack[c:len(needle)+c]
            if sub == needle:
                return c
        return -1

str_1 = "hello"
str_2 = "ll"  
sol = Solution()
res = sol.strStr(str_1, str_2)
print(res)