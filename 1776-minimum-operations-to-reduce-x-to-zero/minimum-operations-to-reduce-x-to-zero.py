class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return - 1

        n = len(nums)
        left, current_sum, max_len = 0, 0, -1

        for right in range(n):
            current_sum += nums[right]
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1