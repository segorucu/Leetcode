from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # if len(beginWord) != len(endWord):
        #     return 0

        # tmplist = []
        # for word in wordList:
        #     if len(word) == len(beginWord):
        #         tmplist.append(word)

        # wordList = tmplist.copy()

        alphabet = set()
        for word in wordList:
            alphabet.update(list(word))

        wordList = set(wordList)
        wordList.add(beginWord)
        graph = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                for letter in alphabet:
                    tmp = word[0:i] + letter + word[i+1:]
                    if tmp in wordList and tmp != word:
                        graph[word].add(tmp)

        queue = collections.deque()
        queue.append((1,beginWord))
        visited = set()
        visited.add(beginWord)
        
        while queue:
            steps, node = queue.popleft()
            if node == endWord:
                return steps
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((steps+1, neigh))

        return 0

            

