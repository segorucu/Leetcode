class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = []
        for l,r,h in buildings:
            events.append((l,h,0))
            events.append((r,h,1))
        events.sort()

        heights = SortedList([0])
        i = 0
        n = len(events)
        ans = []
        while i < n:
            cur_x = events[i][0]
            while i < n and cur_x == events[i][0]:
                x, h, t = events[i]
                if t == 0:
                    heights.add(h)
                else:
                    heights.remove(h)
                i += 1

            if not ans or ans[-1][1] != heights[-1]:
                ans.append((cur_x, heights[-1]))

        return ans

        


        return []