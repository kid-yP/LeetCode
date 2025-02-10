class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarrays(bound: int) -> int:
            count, total = 0, 0
            for num in nums:
                if num <= bound:
                    count += 1
                else:
                    count = 0
                total += count
            
            return total 
    
        return count_subarrays(right) - count_subarrays(left - 1)