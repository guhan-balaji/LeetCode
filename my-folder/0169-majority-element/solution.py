class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_elem = frequency = 0

        for n in nums:
            if frequency == 0:
                majority_elem = n
                frequency += 1
            elif majority_elem == n:
                frequency += 1
            else:
                frequency -= 1
        
        return majority_elem
                
