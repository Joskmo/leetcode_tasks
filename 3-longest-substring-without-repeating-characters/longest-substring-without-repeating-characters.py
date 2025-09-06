class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        longest = 1
        j = 1
        for i in range(len(s)):
            cur_slice = s[i:j]
            while j < len(s) and s[j] not in cur_slice:
                j += 1
                cur_slice = s[i:j]
                cur_len = j - i
                if cur_len > longest:
                    longest = cur_len
        return longest
