class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            is_consecutive_sorted = all(subarray[j] + 1 == subarray[j + 1] for j in range(k - 1))
            
            if is_consecutive_sorted:
                results.append(max(subarray))
            else:
                results.append(-1)

        return results