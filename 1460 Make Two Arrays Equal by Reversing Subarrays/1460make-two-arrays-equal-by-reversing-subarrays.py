class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        c1 = collections.Counter(target)
        c2 = collections.Counter(arr)


        return c1 == c2