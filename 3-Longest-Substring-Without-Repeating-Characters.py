class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = r = 0
        chars = {}
        while r < len(s):
            char = s[r]
            if char in chars and chars[char] >= l:
                l = chars[char] + 1
                chars[char] = r
            else:
                chars[char] = r
            longest = max(longest, r - l + 1)
            r += 1
        return longest