class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        n = len(candies)
        notvisited = set(range(n))
        queue = collections.deque()
        collected = set()
        available_boxes = set()
        for box in initialBoxes:
            available_boxes.add(box)
            if status[box] == 1:
                queue.append(box)
                notvisited.remove(box)

        
        tot = 0
        while queue:
            curr = queue.popleft()

            tot += candies[curr]

            touched = []
            for box in containedBoxes[curr]:
                available_boxes.add(box)
                touched.append(box)
                
            for key in keys[curr]:
                status[key] = 1
                touched.append(key)

            for i in touched:
                if i in available_boxes and status[i] == 1 and i in notvisited:
                    queue.append(i)
                    notvisited.remove(i)
            

        return tot