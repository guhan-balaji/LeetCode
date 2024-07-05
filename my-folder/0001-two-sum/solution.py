class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_idx: Dict[int, int] = dict()

        for idx, num in enumerate(nums):
            if target - num in nums_to_idx:
                return [idx, nums_to_idx[target - num]]
            else:
                nums_to_idx[num] = idx
