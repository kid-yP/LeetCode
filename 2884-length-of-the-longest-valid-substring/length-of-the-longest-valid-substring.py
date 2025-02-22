class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        n = len(word)
        max_length = 0
        left = 0
        
        for right in range(n):
            for length in range(1, 11):
                if right - length + 1 >= left:
                    if word[right - length + 1:right + 1] in forbidden_set:
                        left = right - length + 2
                        break
            
            max_length = max(max_length, right - left + 1)
        
        return max_length