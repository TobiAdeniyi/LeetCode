# Runtime: 52 ms, faster than 70.79% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.5 MB, less than 72.42% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums, target):
        return len([i for i in nums if i < target])