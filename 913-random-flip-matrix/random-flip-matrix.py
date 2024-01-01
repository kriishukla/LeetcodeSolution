class Solution:

    def __init__(self, m: int, n: int):
        self.m,self.n=m,n
        self.reset()

    def flip(self) -> List[int]:
        self.remain-=1
        ridx=random.randint(0,self.remain)
        x=self.mapping[ridx] if ridx in self.mapping else ridx
        self.mapping[ridx]=self.mapping[self.remain] if self.remain in self.mapping else self.remain
        return divmod(x,self.n)

    def reset(self) -> None:
        self.remain=self.m*self.n
        self.mapping=dict()



# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()