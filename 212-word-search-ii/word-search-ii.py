class TrieNode:
    def __init__(self):
        self.child = {}
        self.endword = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.endword = True
            
        
    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.child:
                return False
            curr = curr.child[w]
        return curr.endword
        
       
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m = len(board)
        n = len(board[0])

        vocab = Trie()
        for word in words:
            vocab.insert(word)

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        ans = set()
        def dfs(r,c,trie,wordlist):
            if trie.endword:
                ans.add("".join(wordlist))

            neighs = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in neighs:
                if valid(nr,nc) and (nr,nc) not in visited and board[nr][nc] in trie.child:
                    visited.add((nr,nc))
                    wordlist.append(board[nr][nc])
                    dfs(nr,nc,trie.child[board[nr][nc]],wordlist)
                    wordlist.pop()
                    visited.remove((nr,nc))
            
        trie = vocab.root
        for r in range(m):
            for c in range(n):
                visited = set()
                if board[r][c] in trie.child:
                    visited.add((r,c))
                    dfs(r,c,trie.child[board[r][c]],[board[r][c]])

        # print(ans)
        return list(ans)
