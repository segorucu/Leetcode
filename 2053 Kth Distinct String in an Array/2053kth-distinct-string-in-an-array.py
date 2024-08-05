class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        counter = collections.Counter(arr)
        i = 0
        for key,val in counter.items():
            if val == 1:
                i += 1
            if i == k:
                return key

        return ""
