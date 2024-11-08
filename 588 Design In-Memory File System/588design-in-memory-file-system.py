class TrieNode:
    def __init__(self):
        self.child = {}
        self.files = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def mkdir(self, path) -> None:
        curr = self.root
        for w in path:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]

    def addContent(self, path, file, content):
        curr = self.root
        for w in path:
            curr = curr.child[w]
        if file not in curr.files:
            curr.files[file] = content
        else:
            curr.files[file] += content
            
    def ls(self, path):
        curr = self.root
        for w in path:
            if w not in curr.child:
                return [w]
            curr = curr.child[w]
        
        ans = list(curr.files.keys()) + list(curr.child.keys())
        ans.sort()
        return ans

    def readContent(self, path, file):
        curr = self.root
        for w in path:
            curr = curr.child[w]
        return curr.files[file]
       
class FileSystem:
    def __init__(self):
        self.database = Trie()
        
    def ls(self, path: str) -> List[str]:
        if len(path) > 1:
            path = path[1:].split("/")
            return self.database.ls(path)
        else:
            return self.database.ls([])


    def mkdir(self, path):
        path = path[1:].split("/")
        if path:
            self.database.mkdir(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath[1:].split("/")
        self.database.addContent(path[:-1], path[-1], content)
        

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath[1:].split("/")
        return self.database.readContent(path[:-1], path[-1])

        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)