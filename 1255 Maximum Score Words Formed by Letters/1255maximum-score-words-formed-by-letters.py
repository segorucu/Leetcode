class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        base = ord('a')
        reward = []
        for word in words:
            tot = 0
            for a in word:
                tot += score[ord(a) - base]
            reward.append(tot)

        counter = collections.Counter(letters)

        def backtrack(wi,tot):
            # print(wi,tot)
            if wi == len(words):
                return tot

            word = words[wi]
            one = 0
            for i,a in enumerate(word):
                if counter[a] > 0:
                    counter[a] -= 1
                else:
                    for k in range(i):
                        a = word[k]
                        counter[a] += 1
                    break
            else:
                one = backtrack(wi+1,tot+reward[wi])
                for a in word:
                    counter[a] += 1
            two = backtrack(wi+1,tot)
            return max(one,two)

        return backtrack(0,0)


        