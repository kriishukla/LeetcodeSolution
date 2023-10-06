class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        arr = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if arr[i][j] != -1:
                return arr[i][j]

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            max_path = 1

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(x, y))

            arr[i][j] = max_path
            return max_path

        max_length = 0
        for i in range(m):
            for j in range(n):
                max_length = max(max_length, dfs(i, j))

        return max_length
