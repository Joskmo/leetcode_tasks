class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = int(x / abs(x))
        x_str = str(abs(x))
        reverse = x_str[::-1]
        result = sign * int(reverse)
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
