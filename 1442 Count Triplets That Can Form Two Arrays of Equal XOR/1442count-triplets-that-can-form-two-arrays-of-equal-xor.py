class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        

        n = len(arr)
        count = 0
        for i in range(n):
            a = 0
            for j in range(i,n-1):
                a ^= arr[j]
                b = 0
                for k in range(j+1,n):
                    b ^= arr[k]
                    if a == b:
                        count += 1
                

        return count