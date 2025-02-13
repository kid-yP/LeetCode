class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = {c: 0 for c in 'abc'}
        left = 0
        num_substring = 0

        for right in range(n):
            count[s[right]] += 1

            while all(count[c] > 0 for c in 'abc'):
                num_substring += n - right
                count[s[left]] -= 1
                left += 1

        return num_substring