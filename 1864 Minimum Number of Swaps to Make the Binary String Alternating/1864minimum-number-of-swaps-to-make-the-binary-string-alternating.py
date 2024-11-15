class Solution:
    def minSwaps(self, s: str) -> int:

        ones = s.count("1")
        n = len(s)
        zeros = n - ones
        if abs(ones-zeros) > 1:
            return -1

        if n % 2 == 0:
            first = 0
            for i, val in enumerate(s):
                if i % 2 == 0 and val == "0":
                    first += 1
            second = 0
            for i, val in enumerate(s):
                if i % 2 == 0 and val == "1":
                    second += 1
            return min(first,second)
        elif ones > zeros:
            count = 0
            for i, val in enumerate(s):
                if i % 2 == 0 and val == "0":
                    count += 1
            return count
        else:
            count = 0
            for i, val in enumerate(s):
                if i % 2 == 0 and val == "1":
                    count += 1
            return count
        