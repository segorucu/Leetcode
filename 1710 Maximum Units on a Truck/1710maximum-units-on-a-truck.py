class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes = sorted(boxTypes,key= lambda x: x[1],reverse = True)
        
        tot = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            diff = min(truckSize,boxTypes[i][0])
            tot += diff * boxTypes[i][1]
            truckSize -= diff
            i += 1

        return tot

