class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix, suffix = list(accumulate(nums, operator.mul)), list(accumulate(reversed(nums), operator.mul))[::-1]

        for i in range(len(nums)):
            if i == 0:
                nums[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * suffix[i + 1]
        
        return nums
