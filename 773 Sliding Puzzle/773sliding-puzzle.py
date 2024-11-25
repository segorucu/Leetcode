class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:


        permutations = []
        def backtrack(arr):
            if len(arr) == 6:
                permutations.append((tuple(arr[0:3]),tuple(arr[3:6])))

            for i in range(6):
                if i not in arr:
                    arr.append(i)
                    backtrack(arr)
                    arr.pop()

        arr = []
        backtrack(arr)
        graph = collections.defaultdict(list)
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def valid(r,c):
            return 0 <= r < 2 and 0 <= c < 3

        def findzeroind(tup):
            for r in range(2):
                for c in range(3):
                    if tup[r][c] == 0:
                        return (r,c)

        def swap(tup,r,c,nr,nc):
            arr = [list(inner_tuple) for inner_tuple in tup]
            arr[nr][nc], arr[r][c] = arr[r][c], arr[nr][nc]
            return (tuple(arr[0]),tuple(arr[1]))

        for perm in permutations:
            (r,c) = findzeroind(perm)
            for move in directions:
                nr = r + move[1]
                nc = c + move[0]
                if valid(nr,nc):
                    neigh = swap(perm,r,c,nr,nc)
                    graph[perm].append(neigh)
        
        queue = collections.deque()
        start = (tuple(board[0]),tuple(board[1]))
        goal = ((1,2,3),(4,5,0))
        queue.append((start,0))
        
        seen = set()
        seen.add(start)
        while queue:
            node, it = queue.popleft()
            if node == goal:
                return it

            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    queue.append((neigh,it+1))

        return -1







        