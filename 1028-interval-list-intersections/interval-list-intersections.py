class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

        
        p1 = p2 = 0
        m = len(firstList)
        n = len(secondList)
        res = []
        while p1 < m and p2 < n:
            one = firstList[p1]
            two = secondList[p2]

            s = max(one[0],two[0])
            e = min(one[1],two[1])
            if s <= e:
                res.append([s,e])
            
            if one[1] < two[1]:
                p1 += 1
            else:
                p2 += 1


        return res