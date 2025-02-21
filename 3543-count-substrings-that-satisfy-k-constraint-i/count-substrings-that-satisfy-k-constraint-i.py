class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        n = len(s)
        
        for i in range(n):
            zeros = ones = 0
            for j in range(i, n):
                if s[j] == '0':
                    zeros += 1
                else:
                    ones += 1
                    
                if zeros <= k or ones <= k:
                    count += 1
                else:
                    break
                    
        return count