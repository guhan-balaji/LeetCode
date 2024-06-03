class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_to_idx = {}

        for idx, num in enumerate(nums):
            if target - num in num_to_idx:
                return [idx, num_to_idx[target - num]]
            else:
                num_to_idx[num] = idx
