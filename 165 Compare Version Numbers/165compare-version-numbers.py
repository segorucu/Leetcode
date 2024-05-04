class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        N1 = len(version1)
        N2 = len(version2)

        for p in range(min(N1,N2)):
            if int(version1[p]) < int(version2[p]):
                return -1
            elif int(version1[p]) > int(version2[p]):
                return 1

        if N1 > N2:
            p += 1
            maxval = 0
            for i in range(p,N1):
                # print(p)
                maxval = max(maxval,int(version1[i]))
            if maxval > 0:
                return 1
            else:
                return 0
        elif N2 > N1:
            p += 1
            maxval = 0
            for i in range(p,N2):
                maxval = max(maxval,int(version2[i]))
            if maxval > 0:
                return -1
            else:
                return 0
        else:
            return 0

        
