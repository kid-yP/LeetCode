class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        count = 0
        for num in freq:
            if k > 0 and num + k in freq:
                count += 1
            elif k == 0 and freq[num] > 1:
                count += 1

        return count