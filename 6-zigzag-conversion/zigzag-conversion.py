class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s
        results = [""] * numRows
        cur_line = 1
        direction = 1
        for i in range(len(s)):
            results[cur_line - 1] += s[i]
            if cur_line == numRows:
                direction = -1
            if cur_line == 1 and direction == -1:
                direction = 1
            cur_line += direction
        return "".join(results)
