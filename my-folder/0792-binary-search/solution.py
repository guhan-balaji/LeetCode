class Solution(object):       
    def search(self, nums, target):
        return self.rec_search(0, len(nums) - 1, nums, target)
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

    def rec_search(self, start, end, nums, target):
        if start > end:
            return -1
        
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            return self.rec_search(mid + 1, end, nums, target)
        else:
            return self.rec_search(start, mid - 1, nums, target)
