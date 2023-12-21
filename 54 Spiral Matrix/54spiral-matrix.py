class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])

        smallest = min(m,n)
        nrounds = smallest // 2
        if smallest % 2 == 1:
            nrounds += 1


        leftbound = 0
        rightbound = n - 1
        upperbound = 0
        lowerbound = m - 1
        ans = []
        for roun in range(nrounds):
            i = leftbound
            j = upperbound
            direc = 0
            while True:
                currval = matrix[i][j]
                ans.append(currval)
                if leftbound == rightbound:
                    i += 1
                    if i == lowerbound + 1:
                        break
                elif upperbound == lowerbound:
                    j += 1
                    if j == rightbound + 1:
                        break
                else:
                    if direc == 0:
                        j += 1
                        if j == rightbound:
                            direc = 1
                    elif direc == 1:
                        i += 1
                        if i == lowerbound:
                            direc = 2
                    elif direc == 2:
                        j -= 1
                        if j == leftbound:
                            direc = 3
                    elif direc == 3:
                        i -= 1
                        if i == upperbound:
                            break

            leftbound += 1
            rightbound -= 1
            upperbound += 1
            lowerbound -= 1
        return ans

                




