class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        arr_i=[]
        arr_j=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    arr_i.append(i)
                    arr_j.append(j)
        
        for i in range(0,len(arr_i)):
            for j in range(n):
                matrix[arr_i[i]][j]=0
        
        for i in range(0,len(arr_i)):
            for j in range(m):
                matrix[j][arr_j[i]]=0


        