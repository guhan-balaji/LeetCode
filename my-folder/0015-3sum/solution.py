class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets: Set[Tuple[int, int, int]] = set()

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            start, end = i + 1, len(nums) - 1
            while start < end:
                total = num + nums[start] + nums[end]
                if total == 0:
                    triplets.add((num, nums[start], nums[end]))
                    start, end = start + 1, end - 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1

        return [list(triplet) for triplet in triplets]
