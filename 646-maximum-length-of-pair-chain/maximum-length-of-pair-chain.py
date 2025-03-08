class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        current_end = float('-inf')
        chain_length = 0
        
        for left, right in pairs:
            if left > current_end:
                chain_length += 1
                current_end = right

        return chain_length