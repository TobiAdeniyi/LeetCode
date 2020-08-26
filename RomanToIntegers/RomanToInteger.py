class Solution:
    def romanToInt(self, s):
        syms = ["I", "V", "X", "L", "C", "D", "M"]
        nums = [1, 5, 10,  50, 100, 500, 1000]
        posv = [True, True, True, True, True, True, True]
        
        n = 0
        for i in s[::-1]:
            n += nums[syms.index(i)]
            while posv[syms.index(i)]:
                nums[:syms.index(i)] = [-abs(j) for j in nums[:syms.index(i)]]
                posv[syms.index(i)] = False
        return n
            