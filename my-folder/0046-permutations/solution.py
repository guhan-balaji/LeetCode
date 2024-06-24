class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permute_h(nums, [], [])
    
    def permute_h(self, nums: List[int], permutation: List[int], permutations: List[List[int]]) -> List[List[int]]:
        if len(nums) == 0:
            permutations.append(permutation)
            return permutations

        for i in range(len(permutation)):
            _ = self.permute_h(nums[1:], permutation[:i] + [nums[0]] + permutation[i:], permutations)
        _ = self.permute_h(nums[1:], permutation + [nums[0]], permutations)
        return permutations


        
