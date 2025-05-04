class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        
       
        
        m = len(tasks)
        n = len(workers)
        tasks.sort()
        workers.sort()

        def canfinish(mid):
            n_pills = pills
            queue = deque()
            i = 0
            for j in range(n-mid,n):
                worker = workers[j]

                while i < m and worker + strength >= tasks[i]:
                    queue.append(tasks[i])
                    i += 1

                if not queue:
                    return False
                if worker < queue[0]:
                    if n_pills == 0:
                        return False
                    queue.pop()
                    n_pills -= 1
                else:
                    queue.popleft()
            return True


        left = 0
        right = min(m,n)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            # print(left, right, mid, canfinish(mid))
            if canfinish(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
            
        return res