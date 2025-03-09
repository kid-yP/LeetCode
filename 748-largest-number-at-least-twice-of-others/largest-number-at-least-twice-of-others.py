class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        larg_int = max(nums)
        larg_ind = nums.index(larg_int)

        for i, num in enumerate(nums):
            if i != larg_ind and larg_int < 2 * num:
                return -1

        return larg_ind