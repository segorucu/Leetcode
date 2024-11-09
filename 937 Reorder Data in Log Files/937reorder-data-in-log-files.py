class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letterlogs = []
        digitlogs = []
        for log in logs:
            tmp = log.split()
            if tmp[-1].isdigit():
                digitlogs.append(log)
            else:
                letterlogs.append([tmp[0], tmp[1:]])

        tmparr = list(sorted(letterlogs, key=lambda x: (x[1],x[0])))
        letterlogs = []
        for key, val in tmparr:
            tmp = " ".join([key] + val)
            letterlogs.append(tmp)

        return letterlogs + digitlogs
