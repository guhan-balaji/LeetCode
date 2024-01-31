class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mappings = {}

        for n in nums2:
            while stack and n > stack[-1]:
                mappings[stack[-1]] = n
                stack.pop()
            stack.append(n)
        
        return [mappings.get(n, -1) for n in nums1]

