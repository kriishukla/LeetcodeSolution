class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        bPoint, n = -1, len(arr)
        for i in range(n-2,-1,-1):
            if arr[i] >= arr[i+1]: continue                 
            bPoint = i                                      
            for j in range(n-1,i,-1):                      
                if arr[j] > arr[bPoint]:             
                    arr[j], arr[bPoint] = arr[bPoint], arr[j] 
                    break                                    
            break                                             
        arr[bPoint+1:] = reversed(arr[bPoint+1:])             
            

        