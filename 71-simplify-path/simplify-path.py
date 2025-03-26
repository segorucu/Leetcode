class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")

        stack = []
        for doc in path:
            if len(doc) == 0 or doc[:] == ".":
                pass
            elif doc[:] == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(doc)
        return "/"+"/".join(stack)