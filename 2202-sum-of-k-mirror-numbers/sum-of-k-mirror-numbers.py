class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def createpalindrome(left, odd):
            left = str(left)
            if odd:
                curr = left[0:-1] + left[-1] + left[0:-1][::-1]
                return int(curr)
            else:
                curr = left[:] + left[:][::-1]
                return int(curr)

        
        def convert(num, k):
            curr = []
            while num:
                curr.append(num % k)
                num = num // k
            return curr[:] == curr[::-1]

        sm = 0
        length = 1
        while n:
            for i in range(length, length * 10):
                num = createpalindrome(i, True)
                if convert(num, k):
                    sm += num
                    n -= 1
                if n == 0:
                    break
            if n == 0:
                break
            for i in range(length, length * 10):
                num = createpalindrome(i, False)
                if convert(num, k):
                    sm += num
                    n -= 1
                if n == 0:
                    break
            length *= 10

        return sm
