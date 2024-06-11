class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        counter = collections.Counter(arr1)
        ans = []
        for a in arr2:
            freq = counter[a]
            for i in range(freq):
                ans.append(a)
            del counter[a]

        for key,val in sorted(counter.items()):
            for i in range(val):
                ans.append(key)

        return ans