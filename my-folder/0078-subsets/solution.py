class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def comb(nums: List[int], combination: List[int], combinations: List[List[int]]) -> List[List[int]]:
            if not nums:
                combinations.append(combination)
                return combinations
            
            choose = [nums[0]] + combination
            not_choose = [] + combination

            _ = comb(nums[1:], choose, combinations)
            _ = comb(nums[1:], not_choose, combinations)
            return combinations
        
        return comb(nums, [], [])
