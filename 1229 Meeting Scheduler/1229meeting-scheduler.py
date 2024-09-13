class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        m = len(slots1)
        n = len(slots2)
        slots1.sort()
        slots2.sort()

        j = i = 0
        l1, r1 = slots1[i]
        l2, r2 = slots2[j]
        while (i < m-1 or j < n-1) and min(r1,r2) - max(l1,l2) < duration:
            if (r2 < r1 and j < n-1) or i == m-1:
                j += 1
                l2, r2 = slots2[j]
            else:
                i += 1
                l1, r1 = slots1[i]
        if min(r1,r2) - max(l1,l2) >= duration:
            return [max(l1,l2),max(l1,l2)+duration]

        return []