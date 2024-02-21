class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        

        def calcdiff(s2,state):
            diff = 0
            for a,b in zip(state,s2):
                if a != b:
                    diff += 1
            return diff

        cand1 = cand2 = ""
        for a,b in zip(s1,s2):
            if a != b:
                cand1 += a
                cand2 += b
        s1 = cand1
        s2 = cand2
        n = len(s1)
        if n <= 1:
            return 0

        # mp1 = collections.defaultdict(list)
        # mp2 = collections.defaultdict(list)
        # for i in range(n):
        #     mp1[s1[i]].append(i)
        #     mp2[s2[i]].append(i)

        queue = collections.deque()
        queue.append((s1,0))
        visited = set()
        visited.add(s1)
        mindiff = 30
        while queue:
            state, step = queue.popleft()
            diff = calcdiff(s2,state)
            mindiff = min(diff,mindiff)
            if diff == 0: return step
            for i in range(n):
                one = state[i]
                if one == s2[i]:
                    continue
                for j in range(i+1,n):
                    two = state[j]
                    if two == s2[j]:
                        continue
                    if one != two and two == s2[i]:
                        cand = state[0:i] + two + state[i+1:j] + one + state[j+1:]
                        diff2 = calcdiff(s2,cand)
                        if diff2 <= mindiff and cand not in visited:
                            visited.add(cand)
                            queue.append((cand,step+1))
                            mindiff = diff2
