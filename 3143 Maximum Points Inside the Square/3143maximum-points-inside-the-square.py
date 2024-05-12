class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        
        data = []
        for (x,y),c in zip(points,s):
            loc = max(abs(x),abs(y))
            data.append((loc,c))

        data.sort()
        mp = collections.defaultdict(list)
        for x, ch in data:
            mp[x].append(ch)

        points = 0
        seen = set()
        for key,values in mp.items():
            point = 0
            for val in values:
                if val in seen:
                    return points
                seen.add(val)
                point += 1
            points += point

        return points