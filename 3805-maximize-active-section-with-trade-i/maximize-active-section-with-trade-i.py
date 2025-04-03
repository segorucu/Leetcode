class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
        ones = s.count("1")

        arr = []
        for g,c in groupby(s):
            arr.append((g,len(list(c))))

        zeros = 0
        for i,(g,c) in enumerate(arr):
            if g == "1":
                if 0 < i < len(arr) - 1:
                    print("inside",)
                    zeros = max(zeros, arr[i-1][1] + arr[i+1][1])

        return ones + zeros