# Runtime: 32 ms, faster than 87.92% of Python3 online submissions for Count and Say.
# Memory Usage: 14 MB, less than 37.22% of Python3 online submissions for Count and Say.
import itertools

class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        cas = "1"
        while i < n:
            lst = [''.join(g) for k, g in itertools.groupby(cas)]
            cas = ''
            for chars in lst:
                cas += str(len(chars)) + str(chars[0])
            i += 1
        return cas