class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

                
        mp = collections.defaultdict()
        mp[n-1] = ListNode(n-1)
        for i in range(n-2,-1,-1):
            mp[i] = ListNode(i,mp[i+1])

        dist = n-1
        ans = []
        for u, v in queries:
            # print(u,v)
            if u in mp:
                curr = mp[u].next
                # print(u,v,curr.val)
                while curr.val < v:
                    nxt = curr.next
                    del mp[curr.val]
                    curr = nxt
                    dist -= 1
                if mp[u].next.val < v:
                    mp[u].next = mp[v]
                # print(mp[v].val)
            ans.append(dist)



        return ans
        