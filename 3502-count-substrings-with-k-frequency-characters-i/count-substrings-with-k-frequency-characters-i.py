class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        count = 0
        start = 0
        freq = {}

        for end in range(len(s)):
            char = s[end]
            freq[char] = freq.get(char, 0) + 1

            while any(value >= k for value in freq.values()):
                count += len(s) - end
                char_start = s[start]
                freq[char_start] -= 1
                if freq[char_start] == 0:
                    del freq[char_start]
                start += 1

        return count