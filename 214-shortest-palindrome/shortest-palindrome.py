class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        
        n = len(combined)
        lps = [0] * n
        
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
        
        longest_prefix = lps[-1]
        
        return rev_s[:len(s) - longest_prefix] + s