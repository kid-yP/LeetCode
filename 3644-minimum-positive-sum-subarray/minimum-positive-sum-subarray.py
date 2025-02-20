class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        found = False

        for start in range(len(nums)):
            current_sum = 0
            for end in range(start, min(start + r, len(nums))):
                current_sum += nums[end]
                subarray_len = end - start + 1
                if subarray_len >= l and subarray_len <= r and current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    found = True

        return min_sum if found else -1