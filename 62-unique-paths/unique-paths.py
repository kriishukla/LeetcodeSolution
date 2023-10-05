class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        arr = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

        return arr[m][n]
