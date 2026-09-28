class Solution:
    memo = {}
    def numSquares(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        _sqrt = math.isqrt(n)
        if _sqrt **2 == n:
            self.memo[n] = 1
            return 1
        res = float('inf')
        for k in range(n-1 , 0,-1):
            _sqrt = math.isqrt(k)
            if _sqrt **2 != k:
                continue
            __sqrt = math.isqrt(n-k)
            if __sqrt **2 == n-k:
                self.memo[n] = 2
                return 2 
            res = min(res , 1 + self.numSquares(n - k))
            
        self.memo[n] = res
        return res 
         