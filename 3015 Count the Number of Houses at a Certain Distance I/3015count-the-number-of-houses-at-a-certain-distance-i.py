class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        
        dist = [n*[float("inf")] for _ in range(n)]
        for i in range(n-1):
            dist[i][i] = 0
            dist[i][i+1] = 1
            dist[i+1][i] = 1
         
        dist[x-1][y-1] = 1
        dist[y-1][x-1] = 1
        
        for k in range(n):
 
        # pick all vertices as source one by one
            for i in range(n):

                # Pick all vertices as destination for the
                # above picked source
                for j in range(n):

                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    dist[i][j] = min(dist[i][j],
                                     dist[i][k] + dist[k][j])
        

        arr = n * [0]
        for i in range(n):
            for j in range(n):
                if i != j:
                    arr[dist[i][j]-1] += 1
        
        return arr
        