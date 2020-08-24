class Solution:
    def reverse(self, x):
        str_x = str(x)
        if x<0:
            str_x = '-'+str_x[::-1][:-1]
            x = int(str_x)
            val = x & -0x80000000
            if(val==-0x80000000):
                return x
            else:
                return 0
        else:
            str_x = str_x[::-1]
            x = int(str_x)
            val = x & 0x7fffffff
            if(val==x):
                return x
            else:
                return 0