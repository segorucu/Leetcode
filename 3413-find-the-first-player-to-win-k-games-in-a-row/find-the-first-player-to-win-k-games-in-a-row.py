class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        
        queue = deque()
        for skill in skills:
            queue.append((skill,0))

        n = len(skills)
        if k >= n:
            return skills.index(max(skills))

        while True:
            skilla, ca = queue.popleft()
            skillb, cb = queue.popleft()
            if skilla > skillb:
                ca += 1
                if ca == k:
                    return skills.index(skilla)
                queue.appendleft((skilla,ca))
                queue.append((skillb,cb))
            else:
                cb += 1
                if cb == k:
                    return skills.index(skillb)
                queue.appendleft((skillb,cb))
                queue.append((skilla,ca))