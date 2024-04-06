class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:

        
        ans = []

        i = len(arr1)-1
        j = len(arr2)-1
        carry = 0
        while i >= 0 or j >= 0 or carry != 0:
            one = arr1[i] if i >= 0 else 0
            two = arr2[j] if j >= 0 else 0
            curr = one + two + carry

            carry = 0
            if curr >= 2:
                curr -= 2
                carry -= 1
            elif curr == -1:
                curr = 1
                carry = 1

            ans.append(curr)
            i -= 1
            j -= 1

        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()


        return ans[::-1]

"""

    -32 16 -8 4 -2 1

    [1]  = 1
    [110] = 2
    [100] = 4
    [11010] = 6
    [11000] = 8

    """


        