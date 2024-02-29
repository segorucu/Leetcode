class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        def flip(ind):
            l = 0
            r = ind
            while r > l:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
                l += 1

        ans = []
        n = len(arr)
        val = n
        while val > 1:
            ind = arr.index(val)
            if ind == val - 1:
                val -= 1
            else:
                if ind != 0:
                    ans.append(ind+1)
                    flip(ind)
            ans.append(val)
            flip(val-1)



        return ans
        