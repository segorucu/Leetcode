# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        mat = [[0 for _ in range(n)] for _ in range(m)]

        
        lc = 0
        rc = n-1
        tr = 0
        br = m-1
        direc = "E"
        self.head = head
        

        count = 0
        r = 0
        while count < m*n:
            if direc == "E":
                for c in range(lc,rc+1):
                    mat[r][c] = self.getval()
                    count += 1
                direc = "S"
                tr += 1
            elif direc == "S":
                for r in range(tr,br+1):
                    mat[r][c] = self.getval()
                    count += 1
                direc = "W"
                rc -= 1
            elif direc == "W":
                for c in range(rc,lc-1,-1):
                    mat[r][c] = self.getval()
                    count += 1
                direc = "N"
                br -= 1
            elif direc == "N":
                for r in range(br,tr-1,-1):
                    mat[r][c] = self.getval()
                    count += 1
                direc = "E"
                lc += 1
        return mat

    def getval(self):
            if self.head:
                val = self.head.val
                self.head = self.head.next
            else:
                val = -1
            return val