class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for idx, n in enumerate(nums):
            i, j = idx + 1, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + n == 0:
                        res.add((n, nums[i], nums[j]))
                        i += 1
                        j -= 1
                elif nums[i] + nums[j] + n > 0:
                    j -= 1
                else:
                    i += 1
        
        return res



        
