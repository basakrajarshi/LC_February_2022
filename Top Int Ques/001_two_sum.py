class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(0, len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
                    
        return result

 class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(0, len(nums)):
            j = target - nums[i]
            if j in nums and i != nums.index(j):
                result = [i, nums.index(j)]
                   
        return result
