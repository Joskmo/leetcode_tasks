class Solution:
    def maxArea(self, height: List[int]) -> int:
        A = height
        max_water = 0
        l, r = 0, len(height) - 1
        while(l < r):
            cur_water = min(A[l], A[r]) * (r - l)
            if cur_water > max_water:
                max_water = cur_water
            if A[l] < A[r]:
                l += 1
            else:
                r -= 1
        return max_water

