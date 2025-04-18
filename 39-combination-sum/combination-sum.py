class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, combination: List[int], current_sum: int):
            if current_sum == target:
                result.append(list(combination))
                return
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination, current_sum + candidates[i])
                combination.pop()
        
        backtrack(0, [], 0)
        return result
        