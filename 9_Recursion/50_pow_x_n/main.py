class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        return self.myPow(x * x, n / 2) if n % 2 == 0 else x * pow(x * x, n // 2)