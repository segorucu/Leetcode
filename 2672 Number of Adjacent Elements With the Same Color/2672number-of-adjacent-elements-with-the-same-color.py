class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        
        arr = n * [0]
        ans = []
        union = 0
        for i, col in queries:
            prev = arr[i]
            arr[i] = col
            if prev == col:
                ans.append(union)
                continue
            if i > 0 and prev != 0 and prev == arr[i-1]:
                union -= 1
            if i < n-1 and prev!= 0 and prev == arr[i+1]:
                union -= 1
            if i > 0 and col == arr[i-1]:
                union += 1
            if i < n-1 and col == arr[i+1]:
                union += 1
            ans.append(union)
            
            
        return ans