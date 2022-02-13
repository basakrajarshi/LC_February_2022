class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == None or len(digits) == 0 or digits == "1":
            return ""
        
        digit_to_letter = {'2': ['a', 'b', 'c'],
                           '3': ['d', 'e', 'f'],
                           '4': ['g', 'h', 'i'],
                           '5': ['j', 'k', 'l'],
                           '6': ['m', 'n', 'o'],
                           '7': ['p', 'q', 'r', 's'],
                           '8': ['t', 'u', 'v'],
                           '9': ['w', 'x', 'y', 'z']
                          }
        
        results = []
        
        # Recursive function with letter string and string of digits: params
        def backtrack(combo, nextdigits):
            # If no more digits left
            if len(nextdigits) == 0:
                # add the string to the results
                results.append(combo)
            else:
                # For rach letter belonging to the first digit of the string
                for letter in digit_to_letter[nextdigits[0]]:
                    # Recursively call the backtrack function with
                    # the updated letter string 
                    # and the updated string of digits
                    backtrack(combo + letter, nextdigits[1:])
        
        backtrack("", digits)
        
        return results
