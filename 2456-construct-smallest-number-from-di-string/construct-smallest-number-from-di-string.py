class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        pattern = pattern + "I"
        m = len(pattern)
        q = collections.deque()
        for i in range(1,m+1):
            q.append(str(i))
        # print(pattern)
        ans = m * [""]
        visited = set()
        for i in range(m):
            if i in visited:
                continue
            if pattern[i] == "I":
                val = q.popleft()
                ans[i] = val
                visited.add(i)
            else:
                beg = i
                k = i
                while k < m and pattern[k] == "D":
                    k += 1
                count = k - beg
                k = k - 1
                store = q.popleft()
                for _ in range(count):
                    # print(i,k,q)
                    if not q:
                        break
                    val = q.popleft()
                    ans[k] = val
                    visited.add(k)
                    k -= 1
                q.appendleft(store)
                # print(ans)


        return "".join(ans)
        