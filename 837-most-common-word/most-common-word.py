class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        paragraph = paragraph.lower()
        paragraph = re.split(r'[!?;,.\'\s]+', paragraph)

        # print(paragraph)
        counter = defaultdict(int)
        for a in paragraph:
            if len(a) > 0:
                counter[a] += 1
        # print(counter)
        maxoccurence = 0
        for k,v in counter.items():
            if k in banned:
                continue
            if v > maxoccurence:
                maxoccurence = v
                ans = k

        return ans
