class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in characters:
                characters.remove(s[left])
                left += 1
            
            characters.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len