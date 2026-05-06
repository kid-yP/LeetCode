class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # freq = {}
        
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        
        # for num, count in freq.items():
        #     if count == 1:
        #         return num

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
