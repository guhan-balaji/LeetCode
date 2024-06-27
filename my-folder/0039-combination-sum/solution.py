class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates: List[int], target: int, combination: List[int], \
                      combinations: List[List[int]]) -> List[List[int]]:
            
            if target < 0 or not candidates:
                return combinations
            elif target == 0:
                return combinations.append(combination)
            else:
                ## To ensure unique combinations: candidate list is shrunk
                # choose first and continue with given candidate list
                v = candidates[0]
                _ = backtrack(candidates, target - v, [v] + combination, combinations)

                # dont choose first and discard first from candidate list 
                _ = backtrack(candidates[1:], target, [] + combination, combinations)
                return combinations
            
        return backtrack(candidates, target, [], [])
