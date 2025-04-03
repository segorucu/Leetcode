class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

        maxdate = -1
        ans = []
        m = len(firstList)
        n = len(secondList)
        l1 = l2 = 0
        while l1 < m or l2 < n:
            if l1 < m and l2 < n:
                if firstList[l1][0] < secondList[l2][0]:
                    b,e = firstList[l1]
                    l1 += 1
                elif firstList[l1][0] > secondList[l2][0]:
                    b,e = secondList[l2]
                    l2 += 1
                else:
                    if firstList[l1][1] > secondList[l2][1]:
                        b,e = secondList[l2]
                        l2 += 1
                    else:
                        b,e = firstList[l1]
                        l1 += 1
            else:
                if l1 == m:
                    b,e = secondList[l2]
                    l2 += 1
                else:
                    b,e = firstList[l1]
                    l1 += 1

           
            if b <= maxdate:
                if ans and ans[-1][1] >= b:
                    ans[-1] = [ans[-1][0],b]
                else:
                    ans.append([b,min(maxdate,e)])
            maxdate = max(maxdate,e)

        return ans


