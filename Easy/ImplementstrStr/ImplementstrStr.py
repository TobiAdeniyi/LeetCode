# Runtime: 24 ms, faster than 96.55% of Python3 online submissions for Implement strStr().
# Memory Usage: 14 MB, less than 57.30% of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1