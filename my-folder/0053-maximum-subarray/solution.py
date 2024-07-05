class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = largest_sum = float('-inf')

        for num in nums:
            cur_sum = max(cur_sum + num, num)
            largest_sum = max(largest_sum, cur_sum)
        
        return largest_sum
