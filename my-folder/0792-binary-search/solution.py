class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, target, 0, len(nums) - 1)

    def bin_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        mid = start + (end - start) // 2
        if start > end:
            return -1

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bin_search(nums, target, start, mid - 1)
        else:
            return self.bin_search(nums, target, mid + 1, end)


        
