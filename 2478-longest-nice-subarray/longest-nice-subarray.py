class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_and = 0
        max_len = 0
        
        for right in range(n):
            while (current_and & nums[right]) != 0:
                current_and ^= nums[left]
                left += 1
            current_and |= nums[right]
            max_len = max(max_len, right - left + 1)
        
        return max_len