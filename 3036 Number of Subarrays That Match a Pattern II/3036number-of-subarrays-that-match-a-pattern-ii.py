class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
        def getZarr(string, z):
            n = len(string)
        
            # [L,R] make a window which matches
            # with prefix of s
            l, r, k = 0, 0, 0
            for i in range(1, n):
        
                # if i>R nothing matches so we will calculate.
                # Z[i] using naive way.
                if i > r:
                    l, r = i, i
        
                    # R-L = 0 in starting, so it will start
                    # checking from 0'th index. For example,
                    # for "ababab" and i = 1, the value of R
                    # remains 0 and Z[i] becomes 0. For string
                    # "aaaaaa" and i = 1, Z[i] and R become 5
                    while r < n and string[r - l] == string[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
                else:
        
                    # k = i-L so k corresponds to number which
                    # matches in [L,R] interval.
                    k = i - l
        
                    # if Z[k] is less than remaining interval
                    # then Z[i] will be equal to Z[k].
                    # For example, str = "ababab", i = 3, R = 5
                    # and L = 2
                    if z[k] < r - i + 1:
                        z[i] = z[k]
        
                    # For example str = "aaaaaa" and i = 2, 
                    # R is 5, L is 0
                    else:
        
                        # else start from R and check manually
                        l = i
                        while r < n and string[r - l] == string[r]:
                            r += 1
                        z[i] = r - l
                        r -= 1
        
        # prints all occurrences of pattern 
        # in text using Z algo
        def search(text, pattern):
            concat = pattern + [float("inf")] + text
            l = len(concat)
            z = [0] * l
            getZarr(concat, z)
            count = 0
            for i in range(l):                
                if z[i] == len(pattern):
                    count += 1
            return count
                
        n = len(nums)
        prefix = n * [0]
        prefix[0] = -2
        i = 1
        for one, two in zip(nums[0:n-1],nums[1:n]):
            if one > two:
                prefix[i] = -1
            elif one < two:
                prefix[i] = 1
            i += 1
        
        return search(prefix[1:], pattern)
        