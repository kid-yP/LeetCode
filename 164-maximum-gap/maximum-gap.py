class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        nums.sort()
        max_diff = 0
        for i in range(n - 1):
            max_diff = max(max_diff, nums[i + 1] - nums[i])
            
        return max_diff