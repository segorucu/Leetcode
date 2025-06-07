class Solution:
    def clearStars(self, s: str) -> str:
        
        hp = []
        for i,a in enumerate(s):
            if a != "*":
                heappush(hp,(a,-i))
            else:
                heappop(hp)

        hp.sort(key = lambda x: -x[1])
        ans = []
        for a,i in hp:
            ans.append(a)


        return "".join(ans)