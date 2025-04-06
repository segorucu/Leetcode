class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        vocab = set()
        for st in stickers:
            vocab.update(set(st))

        for t in target:
            if t not in vocab: return -1
        n = len(stickers)

        @cache
        def dp(target):
            if not target:
                return 0

            
            ops = inf
            for i,st in enumerate(stickers):
                counter = Counter(target)
                counter2 = Counter(st)
                intersection = counter & counter2
                if not intersection:
                    continue
                counter -= intersection
                txt = []
                for k in sorted(list(counter.keys())):
                    txt.append(counter[k]*k)
                txt = "".join(txt)
                if (dp(txt)+1) < ops:
                    ops = dp(txt) + 1
            return ops

        target = "".join(sorted(list(target)))
        return dp(target)

