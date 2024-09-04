sys.set_int_max_str_digits(100000)
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        

        if k == 1:
            return n*"9"
        elif k == 2:
            if n <= 2:
                return n*"8"
            return "8" + (n-2)*"9" + "8"
        elif k == 3 or k == 9:
            return n*"9"
        elif k == 5:
            if n <= 2:
                return n*"5"
            return "5" + (n-2)*"9" + "5"
        elif k == 4:
            if n <= 4:
                return n * "8"
            return 2*"8" + (n-4)*"9" + 2*"8"
        elif k == 8:
            if n <= 6:
                return n * "8"
            return 3*"8" +(n-6)*"9" + 3*"8"
        elif k == 7:
            if n <= 2:
                return n*"7"
            left = ((n+1) // 2) * "9"
            while True:
                if n % 2 == 0:
                    c = left + left[::-1]
                else:
                    c = left + left[::-1][1:]
                c = int(c)
                if c % 7 == 0:
                    return str(c)
                left = int(left) - 1
                left = str(left)
        elif k == 6:
            if n <= 2:
                return n*"6"
            left = "8" + ((n-1) // 2) * "9"
            while True:
                if n % 2 == 0:
                    c = left + left[::-1]
                else:
                    c = left + left[::-1][1:]
                sm = 0
                for a in c:
                    sm += int(a)
                if sm % 3 == 0:
                    return c
                left = int(left) - 1
                left = str(left)
 

