class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x >=0 and x <= 9: return True
        order = []
        while (x != 0):
            (x,r) = divmod(x,10)
            order.append(r)
        revorder = order[::-1]
        if order == revorder:
            return True
        else:
            return False
        
        