class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        

        dp[m][n] = True
        

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m:
                    dp[i][j] = dp[i][j] or (dp[i + 1][j] and s1[i] == s3[i + j])
                if j < n:
                    dp[i][j] = dp[i][j] or (dp[i][j + 1] and s2[j] == s3[i + j])
        
        return dp[0][0]
