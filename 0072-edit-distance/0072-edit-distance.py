class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {} 

        def dfs(w1, w2):
            if (w1, w2) in dp:
                return dp[(w1, w2)]

            if not w1 and not w2:
                return 0
            if not w1:
                return len(w2)
            if not w2:
                return len(w1)

            if w1[0] == w2[0]:
                dp[(w1, w2)] = dfs(w1[1:], w2[1:])
            else:

                dp[(w1, w2)] = 1 + min(dfs(w1, w2[1:]),  
                                       dfs(w1[1:], w2),  
                                       dfs(w1[1:], w2[1:]) 
                                      )

            return dp[(w1, w2)]

        return dfs(word1, word2)
