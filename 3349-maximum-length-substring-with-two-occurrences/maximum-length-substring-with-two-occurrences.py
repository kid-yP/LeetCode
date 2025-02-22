class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        char_count = defaultdict(int)
        max_len = 0
        left = 0

        for right in range(n):
            char_count[s[right]] += 1

            while any(count > 2 for count in char_count.values()):
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len