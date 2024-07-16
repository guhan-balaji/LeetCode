class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def rec(nums, permutation: List[int], permutations: List[List[int]]) -> List[List[int]]:
            if len(nums) == 0:
                return permutations.append(permutation)
                

            for i in range(len(permutation)):
                rec(nums[1:], permutation[:i] + [nums[0]] + permutation[i:], permutations)
            rec(nums[1:], permutation + [nums[0]], permutations)

            return permutations
        
        return rec(nums, [], [])
