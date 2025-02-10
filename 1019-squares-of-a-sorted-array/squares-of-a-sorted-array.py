class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        
        for i in range(n):
            res.append(nums[i] ** 2)
        
        res.sort()
        
        return res