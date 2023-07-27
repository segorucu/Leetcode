from collections import deque, defaultdict
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        clips.sort(key = lambda x: (x[0],-x[1]))
        adj = defaultdict(list)
        timetab = defaultdict(tuple)
        visited = set()
        queue = deque()
        for i, clip in enumerate(clips):
            start = clip[0]
            end = clip[1]
            timetab[i] = (start,end)
            if start == 0:
                visited.add(i)
                queue.append((i,1))
            for j in range(i+1,len(clips)):
                if start < clips[j][0] <= end:
                    adj[i].append(j)
                elif clips[j][0] > end:
                    break

        while queue:
            node, step = queue.popleft()
            if timetab[node][1] >= time:
                return step
            for neigh in adj[node]:
                if neigh not in visited:
                    queue.append((neigh,step+1))
                    visited.add(neigh)


        return -1
