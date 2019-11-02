class Solution:
    def fib(self, N):
        if (N == 0):
            return(0)
        Fn_minus1 = 0
        Fn = 1
        tmp = 0
        i = 2
        while (i <= N):
            tmp = Fn
            Fn = Fn + Fn_minus1
            Fn_minus1 = tmp
            i += 1
        return(Fn)
