class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

        concat = firstList + secondList
        concat.sort()
        # print(concat)
        n = len(concat)
        maxdate = concat[0][1]
        ans = []
        for i in range(1,n):
            b,e = concat[i]
            if b <= maxdate:
                if ans and ans[-1][1] >= b:
                    ans[-1] = [ans[-1][0],b]
                else:
                    ans.append([b,min(maxdate,e)])
                # print(ans)
            maxdate = max(maxdate,e)

        return ans


