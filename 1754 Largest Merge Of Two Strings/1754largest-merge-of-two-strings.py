class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        l1 = l2 = 0
        N1 = len(word1)
        N2 = len(word2)
        ans = []
        while l1 < N1 and l2 < N2:
            if word1[l1] > word2[l2]:
                ans.append(word1[l1])
                l1 += 1
            elif word1[l1] < word2[l2]:
                ans.append(word2[l2])
                l2 += 1
            elif word1[l1] == word2[l2]:
                r1, r2 = l1, l2
                while r1 < N1 and r2 < N2:
                    r1 += 1
                    r2 += 1
                    if r1 == N1:
                        ans.append(word2[l2])
                        l2 += 1
                        # for i in range(l2,min(r2+1,N2)):
                        #     ans.append(word2[i])
                        # l2 = i + 1
                        break
                    elif r2 == N2:
                        ans.append(word1[l1])
                        l1 += 1
                        # for i in range(l1,min(r1+1,N1)):
                        #     ans.append(word1[i])
                        # l1 = i + 1
                        break
                    elif word1[r1] > word2[r2]:
                        ans.append(word1[l1])
                        l1 += 1
                        # for i in range(l1,r1+1):
                        #     ans.append(word1[i])
                        # l1 = i + 1
                        break
                    elif word1[r1] < word2[r2]:
                        ans.append(word2[l2])
                        l2 += 1
                        # for i in range(l2,r2+1):
                        #     ans.append(word2[i])
                        # l2 = i + 1
                        break
                
        while l1 < N1:
            ans.append(word1[l1])
            l1 += 1
        while l2 < N2:
            ans.append(word2[l2])
            l2 += 1

        return "".join(ans)

        