class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sub_seq_sum = largest_sum = float("-inf")

        for num in nums:
            cur_sub_seq_sum = max(num, cur_sub_seq_sum + num)
            largest_sum = max(cur_sub_seq_sum, largest_sum)

        return largest_sum
        
