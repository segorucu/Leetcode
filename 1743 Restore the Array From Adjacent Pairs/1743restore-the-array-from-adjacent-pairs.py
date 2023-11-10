from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        m = len(adjacentPairs)
        if m == 1:
            return adjacentPairs[0]

        tab = defaultdict(list)
        ones = set()
        for left, right in adjacentPairs:
            tab[left].append(right)
            tab[right].append(left)
            if left in ones:
                ones.remove(left)
            else:
                ones.add(left)
            if right in ones:
                ones.remove(right)
            else:
                ones.add(right)
        
        ones = list(ones)
        nums = [ones[0]]
        visited = set()
        visited.add(ones[0])
        while True:
            neighbors = tab[nums[-1]]
            if len(neighbors) == 1:
                val = neighbors[0]
            else:
                if neighbors[0] in visited:
                    val = neighbors[1]
                else:
                    val = neighbors[0]
            nums.append(val)
            visited.add(val)
            if val == ones[-1]:
                return nums



        
        