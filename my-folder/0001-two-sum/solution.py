class Solution(object):
    def twoSum(self, nums, target):
        nums_set = set(nums)
        for (i, n) in enumerate(nums):
            if (target - n) in nums_set:
                print(i, n)
                for (j, m) in enumerate(nums):
                    if m == (target - n) and j != i:
                        print(j, m)
                        return [i, j]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
