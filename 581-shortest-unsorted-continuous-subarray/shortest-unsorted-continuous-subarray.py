class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        left, right = 0, n - 1
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        
        if left >= right:
            return 0
        
        subarray_min = min(nums[left:right + 1])
        subarray_max = max(nums[left:right + 1])
        
        while left > 0 and nums[left - 1] > subarray_min:
            left -= 1
        while right < n - 1 and nums[right + 1] < subarray_max:
            right += 1
        
        return right - left + 1