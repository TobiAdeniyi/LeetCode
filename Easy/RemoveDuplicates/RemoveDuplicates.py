# Runtime: 68 ms, faster than 87.82% of Python online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.3 MB, less than 99.66% of Python online submissions for Remove Duplicates from Sorted Array.

class Solution(object):
    def removeDuplicates(self, nums):
        seen = set()
        uniqueNums = [x for x in nums if not (x in seen or seen.add(x))]
        nums[:len(uniqueNums)] = uniqueNums
        return len(uniqueNums)