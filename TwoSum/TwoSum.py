from collections import Counter 
import numpy

class Solution:
    def twoSum(self, nums, target):
        d = dict((val, target - val) for val in num) 
        indx = [idx]
        a = numpy.array(nums)
        b = target - a
        lst = list((Counter(a) & Counter(b)).elements())
        idx = map(lambda x: nums.index(x), lst)
        idx = [i for i in idx if a[i] != b[i]]
        return idx