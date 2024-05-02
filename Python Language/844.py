class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1
        b_s = 0
        b_t = 0
        jump_1 = False
        jump_2 = False

        while i >= -1 or j >= -1:
            if s[i] == '#' and i >= 0:
                b_s += 1
                i-=1
                jump_1 = True
            else:
                if b_s > 0:
                    b_s -=1
                    i-=1
                    jump_1 = True
                else:
                    jump_1 = False
                    
            if t[j] == '#' and j>= 0:
                b_t += 1
                j-=1
                jump_2 = True
            else:
                if b_t > 0:
                    b_t-=1
                    j-=1
                    jump_2 = True
                else:
                    jump_2 = False

            if not jump_1 and not jump_2:   
                if i<0 and j<0:
                    return True
                if s[i] != t[j] or (i<0 and j>=0) or (i>=0 and j<=0):
                    return False
                else:
                    i-=1
                    j-=1
        
        return True

string_1 = "aaa###a"
string_2 = "aaaa###a"

sol = Solution()
res = sol.backspaceCompare(string_1, string_2)
print(res)