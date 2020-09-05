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
# 1. 1
# 2. 11
# 3. 21
# 4. 1211
# 5. 111221
# 6. 312211
# 7. 13112221
# 8. 1113213211
# 9. 31131211131221
#10. 13211311123113112211

"""
If last element in sequences is give in the form:
    input = _ _ _ _ _ _ _ _ _  ...,

we can represent it as:
    input = A B C ...,
    
where A is of length l1 
and contain one charater a,

    A = a a a a a a a a a
        < - - - - - - - >
            l1
    
Then the output is given as:
    outtput = l1 a l2 b l3 c ...

So our algorithm need to:
    1) split input where adjacentt charaters change
    2) calculate lenth of each split and the charater
    3) return 'li char' for each split (thisis wordedreally badly)
"""