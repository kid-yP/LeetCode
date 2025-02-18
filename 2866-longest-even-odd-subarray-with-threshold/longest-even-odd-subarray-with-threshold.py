class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_len = 0
        current_len = 0
        l = 0

        while l < len(nums):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                current_len = 1
                for r in range(l + 1, len(nums)):
                    if nums[r] > threshold or nums[r] % 2 == nums[r - 1] % 2:
                        break
                    current_len += 1
                max_len = max(max_len, current_len)
            l += 1

        return max_len