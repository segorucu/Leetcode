class Solution:
    def minSteps(self, n: int) -> int:
        
        # 3 CPP
        # 4 CPCP
        # 5 CPPPP
        # 6 CPCPP
        # 7 CPPCPP
        # 8 CPCPCP

        rem = n-1
        size = 1
        ops = 0
        def recurse(lastcopy,size,rem):
            if rem <= 0:
                return 0

            if rem == n - 1:
                rem -= 1
                return recurse(lastcopy,size+1,rem) + 2
            if rem % size == 0:
                rem -= size
                return recurse(size,2*size,rem) + 2
            else:
                rem -= lastcopy
                size += lastcopy
                return recurse(lastcopy,size,rem) + 1
            

        return recurse(1,1,n-1)
