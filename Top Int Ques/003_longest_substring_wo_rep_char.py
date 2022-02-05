class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        
        char_present = []
        length = 0
        all_lengths = []
        non_unique = False
        for char in s:
            #print(char)
            if char not in char_present:
                char_present.append(char)
                length += 1
                print(length)
            else:
                non_unique = True
                all_lengths.append(length)
                ind = char_present.index(char)
                char_present = char_present[ind+1::]
                char_present.append(char)
                length = len(char_present)
        
        all_lengths.append(length)
        
        return max(all_lengths)
