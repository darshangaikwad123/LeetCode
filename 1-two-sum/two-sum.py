class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for index,value in enumerate(nums):
            compliment=target-value
            #print(compliment)
            if compliment in seen:
                return [seen[compliment],index]
            seen[value]=index