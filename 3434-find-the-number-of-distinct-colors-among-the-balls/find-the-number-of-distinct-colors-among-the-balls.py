class Solution:
    def remove(self, counter, prev):
        counter[prev] -= 1
        if counter[prev] == 0:
            del counter[prev]

    def add(self, counter, col):
        if col in counter:
            counter[col] += 1
        else:
            counter[col] = 1

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        colours = {}
        counter = {}
        m = len(queries)

        ans = m * [None]
        for i,q in enumerate(queries):
            ind, col = q[0], q[1]
            if ind not in colours:
                self.add(counter, col)
            elif colours[ind] == col:
                pass
            else:
                prev = colours[ind]
                self.remove(counter, prev)
                self.add(counter, col)
                
            ans[i] = len(counter.keys())
            colours[ind] = col
        return ans