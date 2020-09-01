# Runtime: 56 ms, faster than 15.65% of Python3 online submissions for Remove Element.
# Memory Usage: 13.9 MB, less than 46.52% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums, val):
        j = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j