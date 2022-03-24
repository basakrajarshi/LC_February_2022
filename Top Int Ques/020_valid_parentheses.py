class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        
        d = {")":"(",
             "}":"{",
             "]":"["}
        
        if len(s) % 2 != 0 or s[0] in d.keys():
            return False
        
        stack = []
        for i in range(len(s)):
            if s[i] in d.keys():
                if len(stack) == 0:
                    return False
                elif stack[-1] == d[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        if len(stack) == 0:
            return True
        
        return False
