class Solution:
    def firstUniqChar(self, s: str) -> int:
        stack = []
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
            stack.append(char)

        for i, char in enumerate(stack):
            if freq[char] == 1:
                return i

        return -1