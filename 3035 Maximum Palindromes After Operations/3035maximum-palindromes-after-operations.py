class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        
        counter = collections.defaultdict(int)
        for word in words:
            for a in word:
                counter[a] += 1

        pairs = 0
        for key,val in counter.items():
            pairs += val // 2
            
        words = sorted(words, key=len)
        
        count = 0
        for word in words:
            if len(word) == 1:
                count += 1
            else:
                needed = len(word) // 2
                if needed <= pairs:
                    pairs -= needed
                    count += 1
                else:
                    break
                    
                    
        return count
        