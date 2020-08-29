# Runtime: 28 ms, faster than 98.89% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.7 MB, less than 84.47% of Python3 online submissions for Merge Two Sorted Lists.

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        