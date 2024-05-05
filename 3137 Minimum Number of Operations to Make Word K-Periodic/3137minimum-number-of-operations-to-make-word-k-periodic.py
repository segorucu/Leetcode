class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        
        counter = collections.defaultdict(int)

        n = len(word)
        reps = n // k
        for i in range(reps):
            start = i * k
            end = start + k
            counter[word[start:end]] += 1
        
        maxval = max(counter.values())

        # print(maxval,counter)


        return reps - maxval