class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #like combination sum ii 
        res = []

        def dfs(i, curr, total ):
            #base cases
            if len(curr) == k and total == n:
                res.append(curr.copy())
                return 
            if i > 9 or total > n:
                return 
            
            curr.append(i)
            dfs(i+1, curr, total+ i)
            curr.pop()
            dfs(i+1, curr, total)

        
        dfs(1, [], 0)
        return res
