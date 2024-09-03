# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':

        mp = collections.defaultdict(int)
        curr = poly1
        while curr:
            mp[curr.power] = curr.coefficient
            curr = curr.next
        curr = poly2
        while curr:
            mp[curr.power] += curr.coefficient
            if mp[curr.power] == 0:
                del mp[curr.power]
            curr = curr.next

        keylist = list(mp.keys())
        keylist.sort(reverse = True)
        Sentinel = PolyNode()
        curr = Sentinel
        for key in keylist:
            curr.next = PolyNode(mp[key],key)
            curr = curr.next

        return Sentinel.next

        

        
        