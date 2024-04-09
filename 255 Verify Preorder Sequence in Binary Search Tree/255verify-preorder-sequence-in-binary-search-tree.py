class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:

        stack = []
        minlimit = -inf
        for num in preorder:
            while stack and stack[-1] < num:
                minlimit = stack.pop()

            if num < minlimit:
                return False

            stack.append(num)

        return True
        