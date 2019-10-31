class Solution:
    def isValid(self, s):
        if (type(s) is not str or len(s) & 1):
            return(False)
        elif (s == ""):
            return(True)
        CLOSING_PAR = {"(": ")", "[": "]", "{": "}", ")": "(", "]": "[", "}": "{"}
        OPP_PAR = {"(": True, "[": True, "{": True, ")": False, "]": False, "}": False}
        i = 0
        stack = []
        s_len = len(s)
        while(i < s_len):
            if (OPP_PAR[s[i]] == True):
                stack.append(s[i])
            elif (stack and CLOSING_PAR[stack[-1]] == s[i]):
                stack.pop()
            else:
                return(False)
            i += 1
        if (stack == []):
            return(True)
        return(False)
