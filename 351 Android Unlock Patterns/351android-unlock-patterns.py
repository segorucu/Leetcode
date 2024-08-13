class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        visited = set()


        invalid = {
            (1,3),(3,1),(1,9),(9,1),(1,7),(7,1),(3,9),(9,3),(3,7),(7,3),
            (2,8),(8,2),(4,6),(6,4),(7,9),(9,7)
        }

        def recurse(i):
            if m <= len(curr) <= n:
                tup = tuple(curr)
                if tup not in visited:
                    # print(tup)
                    visited.add(tup)

            if len(curr) < n:
                for j in range(1,10):
                    if j in curr:
                        continue
                    if (i,j) in invalid and (i+j) // 2 not in curr:
                        continue
                    curr.append(j)
                    recurse(j)
                    curr.pop()
                    
        for i in range(1,10):
            curr = [i]
            recurse(i)
        # print(visited)

        return len(visited)