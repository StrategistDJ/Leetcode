class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        brack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                brack.append(s[i])
            else:
                if len(brack) > 0:
                    if s[i] == ')' and brack[-1] == '(':
                        brack.pop(-1)
                    elif s[i] == ']' and brack[-1] == '[':
                        brack.pop(-1)
                    elif s[i] == '}' and brack[-1] == '{':
                        brack.pop(-1)
        
        if len(brack) > 0:
            return False
        else: 
            return True 

bracket = "([}}])"
sol = Solution()
res = sol.isValid(bracket)
print(res)