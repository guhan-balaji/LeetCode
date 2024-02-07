class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = sub_array_sum = float('-inf')

        for n in nums:
            sub_array_sum = n if n > n + sub_array_sum else n + sub_array_sum
            max_sum = max_sum if max_sum > sub_array_sum else sub_array_sum 
        
        return max_sum
