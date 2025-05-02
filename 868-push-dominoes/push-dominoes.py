class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        statemp = defaultdict(tuple)
        n = len(dominoes)
        queue = deque()
        for i,state in enumerate(dominoes):
            if state != ".":
                queue.append((i,state,0))
            statemp[i] = (state,0)

        while queue:
            i, state, time = queue.popleft()
            if state == "R":
                j = i + 1
            else:
                j = i - 1
            if 0 <= j < n:
                if statemp[j][0] == ".":
                    if 1 <= j < n-1 and statemp[j-1][0] == "R" and statemp[j+1][0] == "L"\
                        and statemp[j-1][1] == statemp[j+1][1]:
                        pass
                    else:
                        statemp[j] = (state,time+1)
                        queue.append((j,state,time+1))

        ans = n*[""]
        for k,v in statemp.items():
            ans[k] = v[0]

        return "".join(ans)


