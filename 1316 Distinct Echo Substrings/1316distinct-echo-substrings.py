class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        n = len(text)
        hashing = n * [0]
        base = ord('a')-1
        curr = 0
        for i, a in enumerate(text):
            curr += (ord(a) - base) * 26 ** i
            hashing[i] = curr
        
        count = 0
        seen = set()
        for left in range(n-1):
            width = 1
            r1 = left + width - 1 
            r2 = left + 2 * width - 1
            while r2 < n:
                if left > 0:
                    leftside = (hashing[r1]-hashing[left-1]) // 26 ** left
                    rightside = (hashing[r2]-hashing[r1]) // 26 ** (r1+1)
                else:
                    leftside = hashing[r1]
                    rightside = (hashing[r2]-hashing[r1]) // 26 ** (r1+1)
                if leftside == rightside and leftside not in seen:
                    seen.add(leftside)
                    count += 1
                width += 1
                r1 = left + width - 1 
                r2 = left + 2 * width - 1


        return count

        