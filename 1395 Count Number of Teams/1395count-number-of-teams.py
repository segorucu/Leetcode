from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating: List[int]) -> int:

        sortedlist = SortedList()
        sortedlist.update(rating)
        higher = []
        
        n = len(sortedlist)
        for i in range(n):
            curr = rating[i]
            loc = sortedlist.index(curr)
            higher.append(n-loc-i-1)
            sortedlist.remove(curr)

        ans = 0
        for i in range(n-1):
            prev = rating[i]
            for j in range(i+1,n):
                curr = rating[j]
                if curr > prev:
                    ans += higher[j]
                else:
                    ans += (n-j-1-higher[j])


        return ans
        