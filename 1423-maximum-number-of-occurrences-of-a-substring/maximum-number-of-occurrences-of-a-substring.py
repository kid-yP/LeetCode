class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        substring_count = defaultdict(int)
        max_occurrences = 0

        for i in range(n - minSize + 1):
            substring = s[i:i + minSize]
            if len(set(substring)) <= maxLetters:
                substring_count[substring] += 1
                max_occurrences = max(max_occurrences, substring_count[substring])
            
        return max_occurrences