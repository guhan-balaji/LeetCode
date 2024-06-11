class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set([])

        for i, n in enumerate(nums):
            if n > 0:
                break

            l, r = i + 1, len(nums) - 1

            while l < r:
                if n + nums[l] + nums[r] == 0:
                    triplets.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif n + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        
        return [list(triplet) for triplet in triplets]
