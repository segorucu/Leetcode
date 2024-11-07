"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        return copy.deepcopy(head)
        if not head:
            return None
        mp = defaultdict()
        idmap = defaultdict()
        curr = head
        i = 0
        prev = None
        while curr:
            mp[i] = Node(curr.val)
            idmap[curr] = i
            if prev:
                prev.next = mp[i]
            prev = mp[i]
            curr = curr.next
            i += 1

        i = 0
        curr = head
        while curr:
            if curr.random:
                j = idmap[curr.random]
                mp[i].random = mp[j]
            curr = curr.next

            i += 1

        return mp[0]
