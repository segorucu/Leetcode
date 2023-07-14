from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:

        forward = defaultdict(list)
        inDegree = defaultdict(int)
        letters = set()
        for i, word in enumerate(words):
            for j,letter in enumerate(word):
                if letter not in letters:
                    letters.add(letter)
            if i != len(words)-1:
                nxt= words[i+1]
                for j in range(len(word)):
                    if j == len(nxt):
                        return ""
                    if word[j] != nxt[j]:
                        forward[word[j]].append(nxt[j])
                        inDegree[nxt[j]] += 1
                        break
                if j == len(word):
                    if len(nxt) > len(word):
                        return ""

        queue = deque()
        nletters = len(letters)
        letters = list(letters)
        for i, letter in enumerate(letters):
            if inDegree[letter] == 0:
                queue.append(letter)

        ans = ""
        while queue:
            letter = queue.popleft()
            ans += letter
            for neigh in forward[letter]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    queue.append(neigh)

        if len(ans) != nletters:
            return ""

        return ans




