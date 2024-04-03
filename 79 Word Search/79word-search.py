class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        m = len(board)
        n = len(board[0]) 

        
        def valid(ni,nj):
            if 0 <= ni < m and 0 <= nj < n and (ni,nj) not in visited:
                return True
            return False

        def backtrack(i,j,curr):
            if len(curr) == len(word):
                return True

            for move in directions:
                ni = i + move[1]
                nj = j + move[0]
                if valid(ni,nj):
                    loc = len(curr)
                    if word[loc] == board[ni][nj]:
                        visited.add((ni,nj))
                        curr += board[ni][nj]
                        if backtrack(ni,nj,curr):
                            return True
                        visited.remove((ni,nj))
                        curr = curr[:-1]
            return False

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    visited = set()
                    visited.add((i,j))
                    if backtrack(i,j,word[0]):
                        return True
        return False

        