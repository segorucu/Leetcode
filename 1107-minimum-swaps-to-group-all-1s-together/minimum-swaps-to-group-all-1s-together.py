class Solution:
    def minSwaps(self, data: List[int]) -> int:
        

        ones = data.count(1)

        zeros = 0
        l = r = 0
        n = len(data)
        for r in range(ones):
            if data[r] == 0:
                zeros += 1
        ans = zeros
        
        while r < n-1:
            r += 1
            if data[r] == 0:
                zeros += 1
            if data[l] == 0:
                zeros -= 1
            l += 1
            ans= min(ans,zeros)
        return ans