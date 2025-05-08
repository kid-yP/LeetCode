class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if sorted(s1) != sorted(s2): 
            return False
        
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    for split in range(1, k):
                        if (dp[i][j][split] and dp[i + split][j + split][k - split]) or \
                           (dp[i][j + k - split][split] and dp[i + split][j][k - split]):
                            dp[i][j][k] = True
                            break
        
        return dp[0][0][n]