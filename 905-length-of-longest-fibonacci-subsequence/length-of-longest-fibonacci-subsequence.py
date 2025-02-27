class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        

        visited = set(arr)

        n = len(arr)
        ans = 1
        for i in range(n):
            
            for j in range(i+1,n):
                curr = arr[j]
                prev = arr[i]
                count = 2
                while (prev+curr) in visited:
                    prev, curr = curr, prev+curr
                    count += 1
                ans = max(ans,count)


        if ans <= 2:
            return 0
        return ans
