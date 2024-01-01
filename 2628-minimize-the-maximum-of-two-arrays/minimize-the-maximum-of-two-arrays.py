class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def bs(self, l, h, divisor1, divisor2, lcm, ans, c1, c2):
        if l <= h:
            m = (l + h) // 2
            
            a = m - (m // divisor1)
            b = m - (m // divisor2)
            c = m - (m // divisor1) - (m // divisor2) + (m // lcm)
            
            if a >= c1 and b >= c2 and a + b - c >= c1 + c2:
                ans[0] = m
                self.bs(l, m - 1, divisor1, divisor2, lcm, ans, c1, c2)
            else:
                self.bs(m + 1, h, divisor1, divisor2, lcm, ans, c1, c2)
    
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        g = self.gcd(max(divisor1, divisor2), min(divisor1, divisor2))
        l = (divisor1 * divisor2) // g
        
        ans = [1000000000]
        
        self.bs(2, 10000000000, divisor1, divisor2, l, ans, uniqueCnt1, uniqueCnt2)
        
        return int(ans[0])

        
        