"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        mp = {}
        values = []
        curr = head
        i = 0
        while curr:
            mp[curr] = i
            values.append(curr.val)
            curr = curr.next
            i += 1

        random = {}
        i = 0
        curr = head
        while curr:
            if curr.random:
                random[i] = mp[curr.random]
            curr = curr.next
            i += 1

        # print(random)

        Sentinel = Node(0)
        curr = Sentinel
        newmp = {}
        for i in range(len(values)):
            curr.next = Node(values[i])
            curr = curr.next
            newmp[i] = curr

        curr = Sentinel
        curr = curr.next
        for i in range(len(values)):
            if i in random:
                curr.random = newmp[random[i]]
            curr = curr.next


        return Sentinel.next
        