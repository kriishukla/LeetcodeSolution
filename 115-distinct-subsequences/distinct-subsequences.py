class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = {}  

        def fn(s, t, m, n):
            if (m, n) in dp:
                return dp[(m, n)]

            if n == 0:
                return 1
            if m == 0:
                return 0

            if s[m - 1] == t[n - 1]:
                x = fn(s, t, m - 1, n - 1)
                y = fn(s, t, m - 1, n)
                total = x + y
            else:

                total = fn(s, t, m - 1, n)

            dp[(m, n)] = total
            return total

        return fn(s, t, m, n)
