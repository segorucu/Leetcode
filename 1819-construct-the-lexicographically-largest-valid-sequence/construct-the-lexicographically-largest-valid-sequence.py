class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
    
        m = 2*n-1
        arr = m * [0]
        used = set()

        def backtrack(i):
            if m == i:
                return True

            for k in range(n,0,-1):

                if k in used:
                    continue

                if k > 1 and (i+k >= m or arr[i+k]):
                    continue

                used.add(k)
                arr[i] = k
                if k > 1:
                    arr[i+k] = k

                r = i + 1
                while r < m  and arr[r]:
                    r += 1
                if backtrack(r):
                    return True

                used.remove(k)
                arr[i] = 0
                if k > 1:
                    arr[i+k] = 0

            return False

        backtrack(0)

        return arr[:]