class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(l,r):
            while l < r:
                s[r], s[l] = s[l], s[r]
                r -= 1
                l += 1

        n = len(s)
        reverse(0,n-1)
        l = 0
        for i,a in enumerate(s):
            if a == " ":
                reverse(l,i-1)
                l = i+1
        reverse(l,n-1)
        # print(s)

        return 
        