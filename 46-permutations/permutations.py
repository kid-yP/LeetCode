class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current_permutation):
            if len(current_permutation) == len(nums):
                results.append(current_permutation[:])
                return
            
            for num in nums:
                if num in current_permutation:
                    continue
                
                current_permutation.append(num)
                backtrack(current_permutation)
                current_permutation.pop()
        
        results = []
        backtrack([])
        return results