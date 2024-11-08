class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        common = set(arr1) & set(arr2)
        ans = []
        for a in arr3:
            if a in common:
                ans.append(a)

        return ans