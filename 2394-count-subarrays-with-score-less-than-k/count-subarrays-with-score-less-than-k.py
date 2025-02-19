class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        start = 0
        current_sum = 0

        for end in range(len(nums)):
            current_sum += nums[end]
            while current_sum * (end - start + 1) >= k and start <= end:
                current_sum -= nums[start]
                start += 1
            count += (end - start + 1)

        return count