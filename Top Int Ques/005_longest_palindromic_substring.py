class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand (s, l, r):
            while (l >= 0 and r <= len(s) - 1 and s[r] == s[l]):
                l -= 1
                r += 1
            return r - l - 1
        
        if s == None or len(s) == 0:
            return ''
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            len1 = expand(s, i, i)
            len2 = expand(s, i, i+1)
            maxl = max(len1, len2)
            
            if maxl > end - start:
                start = i - (maxl-1)//2
                end = i + (maxl)//2
                
        return s[start:end+1]

    class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        reslen = 0
        
        for i in range(len(s)):
            # odd length
            l = i
            r = i
            while (l >= 0 and r < len(s) and s[r] == s[l]):
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1
            
            # even length
            l =  i
            r = i+1
            while (l >= 0 and r < len(s) and s[r] == s[l]):
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1
                
        return res
