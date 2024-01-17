class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        visited = set()
        for key,val in counter.items():
            if val not in visited:
                visited.add(val)
            else:
                return False
        return True
        