class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = w = b = 0

        for n in nums:
            match n:
                case 0:
                    r += 1
                case 1:
                    w += 1
                case 2:
                    b += 1
                case _:
                    print("unknown color.")
        
        nums[:r] = [0] * r
        nums[r: r+w] = [1] * w
        nums[r+w:r+w+b]= [2] * b
