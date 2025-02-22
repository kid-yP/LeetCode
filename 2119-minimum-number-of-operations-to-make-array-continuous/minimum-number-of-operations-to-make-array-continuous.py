class Solution:
    def minOperations(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))
        n = len(unique_nums)
        total_length = len(nums)
        
        max_length = 0
        left = 0
        
        for right in range(n):
            while unique_nums[right] - unique_nums[left] > total_length - 1:
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return total_length - max_length