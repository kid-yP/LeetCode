from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        ps = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                ps[start] += 1
                ps[end + 1] -= 1
            else:
                ps[start] -= 1
                ps[end + 1] += 1
        
        for i in range(1, n):
            ps[i] += ps[i - 1]
        
        result = []
        for i in range(n):
            curr_pos = ord(s[i]) - ord('a')
            new_pos = (curr_pos + ps[i]) % 26
            result.append(chr(new_pos + ord('a')))
        
        return "".join(result)