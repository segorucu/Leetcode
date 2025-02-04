class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        
        def concat(str1,str2):
            N1, N2 = len(str1), len(str2)
            if N1 <= N2:
                if str1 in str2:
                    return str2
            else:
                if str2 in str1:
                    return str1
            minlen = min(N1,N2)
            ans = str1 + str2
            for i in range(minlen):
                if str1[-i-1:] == str2[0:i+1]:
                    ans = str1[0:-i-1] + str2
                    # print(ans,i)
            return ans

        def compare(st1,st2):
            if len(st2) < len(st1):
                st1 = st2
            elif len(opt) == len(ans):
                st1 = min(st1,st2)
            return st1

        ans = concat(concat(a,b),c)
        opt = concat(concat(a,c),b)
        ans = compare(ans,opt)
        opt = concat(concat(b,a),c)
        ans = compare(ans,opt)
        opt = concat(concat(b,c),a)
        ans = compare(ans,opt)
        opt = concat(concat(c,a),b)
        ans = compare(ans,opt)
        opt = concat(concat(c,b),a)
        ans = compare(ans,opt)
        return ans
        