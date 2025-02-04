class Solution:
    def is_subsequence(self, s1: str, s2: str) -> bool:
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        
        return i == len(s1)

    def findLUSlength(self, strs: List[str]) -> int:
        max_length = -1
        n = len(strs)

        for i in range(n):
            is_uncommon = True
            for j in range(n):
                if i != j and self.is_subsequence(strs[i], strs[j]):
                    is_uncommon = False
                    break
            if is_uncommon:
                max_length = max(max_length, len(strs[i]))

        return max_length