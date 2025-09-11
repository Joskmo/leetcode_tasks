class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l, r = 0, len(height) - 1
        while(l < r):
            cur_water = min(height[l], height[r]) * (r - l)
            if cur_water > max_water:
                max_water = cur_water
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water

