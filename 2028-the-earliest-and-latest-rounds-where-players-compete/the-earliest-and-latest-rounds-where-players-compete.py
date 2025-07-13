class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        
        arr = []
        for i in range(1,n+1):
            arr.append(i)

        mainqueue = deque()
        mainqueue.append((1,arr[:]))

        def backtrack(i, tmparr):
            if i == len(arr) // 2:
                if len(arr) % 2:
                    tmparr.append(arr[i])
                queue.append(tmparr[:])
                if len(arr) % 2:
                    tmparr.pop()
                return

            tmparr.append(arr[i])
            backtrack(i+1, tmparr)
            tmparr.pop()
            tmparr.append(arr[n-i-1])
            backtrack(i+1, tmparr)
            tmparr.pop()


        wanted = set()
        wanted.add(firstPlayer)
        wanted.add(secondPlayer)  

        ans = []
        while mainqueue:
            loop, arr = mainqueue.popleft()
            n = len(arr)
            for i in range(n//2):
                if arr[i] in wanted and arr[n-i-1] in wanted:
                    if len(ans) < 2:
                        ans.append(loop)
                    else:
                        ans[-1] = loop
            if n > 1:
                queue = []
                backtrack(0, [])
                for q in queue:
                    if firstPlayer in q and secondPlayer in q:
                        q.sort()
                        mainqueue.append((loop+1, q[:]))

        if len(ans) == 1:
            ans.append(ans[0]) 
        return ans
