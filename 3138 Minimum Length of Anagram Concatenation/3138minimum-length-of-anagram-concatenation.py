class Solution:
    def minAnagramLength(self, s: str) -> int:

        counter = collections.Counter(s)
        values = list(counter.values())
        gcd = math.gcd(*values)
        req = len(s) // gcd
        maxsize = len(s)
        for size in range(1,maxsize+1):
            if maxsize % size == 0 and size % req == 0:
                counter0 = collections.Counter(s[0:size])
                for i in range(size,len(s),size):
                    counter1 = collections.Counter(s[i:i+size])
                    if counter0 != counter1:
                        break
                else:
                    return size




        return len(s)
        