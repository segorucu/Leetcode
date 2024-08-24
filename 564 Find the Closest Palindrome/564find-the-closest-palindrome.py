class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        num = [int(n[i]) for i in range(len(n))]
        N = len(n)
        if N == 1:
            return str(int(n)-1)

        l = 0
        r = N - 1

        if N % 2 == 0:
            l = N // 2 - 1
            r = l+1
            odd = False
        else:
            l = N // 2 - 1
            r = l+2
            odd = True
            m = N // 2

        possibilities = []
        if odd:
            # option 1
            first_half = n[0:l+1]
            cand = n[0:l+1] + n[m] + first_half[::-1]
            possibilities.append(int(cand))

            # option 2
            tmp = int(first_half + n[m]) + 1
            tmp = str(tmp)
            cand = tmp[0:-1] + tmp[-1] + tmp[0:-1][::-1]
            possibilities.append(int(cand))

            # option 3
            tmp = int(first_half + n[m]) - 1
            tmp = str(tmp)
            cand = tmp[0:-1] + tmp[-1] + tmp[0:-1][::-1]
            possibilities.append(int(cand))

        else:
            # option 1
            first_half = n[0:l+1]
            cand = n[0:l+1] + first_half[::-1]
            possibilities.append(int(cand))

            # option 2
            tmp = int(first_half) + 1
            tmp = str(tmp)
            cand = tmp + tmp[::-1]
            possibilities.append(int(cand))

            # option 2
            tmp = int(first_half) - 1
            tmp = str(tmp)
            cand = tmp + tmp[::-1]
            possibilities.append(int(cand))

        tmp = 10 ** (N) + 1
        possibilities.append(tmp)
        tmp = 10 ** (N-1) - 1
        possibilities.append(tmp)
        # print(possibilities)

        diff = inf
        for poss in possibilities:
            if poss == int(n):
                continue
            elif abs(poss-int(n)) < diff:
                diff = abs(poss-int(n))
                ans = poss
            elif abs(poss-int(n)) == diff:
                ans = min(ans,poss)


        return str(ans)