class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def c_sum(candidates: List[int], target: int, 
                  combination: List[int] = [], combinations: List[int] = []) -> List[List[int]]:
            
            if not candidates or target < 0: 
                return combinations
            elif target == 0:
                return combinations.append(combination)
            
            c = candidates[0]
            # choose candidate
            c_sum(candidates[:], target - c, combination[:] + [c], combinations)
            
            # discard candidate
            c_sum(candidates[1:], target, combination[:], combinations)
            
            return combinations
        
        return c_sum(candidates, target)
