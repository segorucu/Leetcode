class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        arr = [str(i) for i in range(1,n+1)]
        arr.sort()
        arr = [int(arr[i]) for i in range(n)]

        return arr