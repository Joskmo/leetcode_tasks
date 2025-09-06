class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = (m + n)
        half = total // 2
        # Гарантируем, что nums1 короче nums2
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        l, r = 0, m - 1
        while 1:
            i = (l + r) // 2 # index
            j = half - i - 2 # index
            left1 = nums1[i] if i >= 0 else float("-infinity")
            right1 = nums1[i + 1] if (i + 1) < m else float("infinity")
            left2 = nums2[j] if j >= 0 else float("-infinity")
            right2 = nums2[j + 1] if (j + 1) < n else float("infinity")
            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return float(min(right1, right2))
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1