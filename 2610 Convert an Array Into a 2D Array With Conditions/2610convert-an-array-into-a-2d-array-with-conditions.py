from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        n = max(counter.values())
        arr = [[] for _ in range(n)]
        
        for key, val in counter.items():
            for i in range(val):
                # print(i,val,arr)
                arr[i].append(key)

        return arr