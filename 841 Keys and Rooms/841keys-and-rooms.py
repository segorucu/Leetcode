from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        opened = set()
        def dfs(node):
            if node not in opened:
                opened.add(node)
                for val in rooms[node]:
                    dfs(val)

        dfs(0)
        


        return len(opened) == len(rooms)