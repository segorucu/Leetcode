from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.append(beginWord)

        m = len(beginWord)
        mp = defaultdict(list)
        for word in wordList:
            for word2 in wordList:
                if word == word2:
                    continue
                diff = 0
                for c1,c2 in zip(word,word2):
                    if c1 != c2:
                        diff += 1
                if diff == 1:
                    mp[word].append(word2)

        queue = deque()
        queue.append((beginWord,0))
        visited = set()
        ans = []
        depthmap = defaultdict(list)
        while queue:
            node, depth = queue.popleft()
            visited.add(node)
            depthmap[depth].append(node)
            if node == endWord:
                break
            for neigh in mp[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh,depth+1))

        def dfs(path,depth):
            if depth == 0:
                newpath = path.copy()
                newpath.append(beginWord)
                newpath.reverse()
                ans.append(newpath[:])
                return

            for neigh in depthmap[depth]:
                diff = 0
                for c1,c2 in zip(path[-1],neigh):
                    if c1 != c2:
                        diff += 1
                if diff == 1:
                    path.append(neigh)
                    dfs(path,depth-1)
                    path.pop()

        maxdepth = max(depthmap.keys())
        dfs([endWord],maxdepth-1)

        return ans
        