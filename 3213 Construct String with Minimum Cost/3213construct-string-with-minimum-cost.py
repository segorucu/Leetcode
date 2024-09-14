from functools import cache
class TrieNode:
    def __init__(self):
        # Initialize TrieNode attributes
        self.children = {}
        self.output = []
        self.fail = None

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:

        def build_automaton(keywords):
            # Initialize root node of the trie
            root = TrieNode()

            # Build trie
            for keyword in keywords:
                node = root
                # Traverse the trie and create nodes for each character
                for char in keyword:
                    node = node.children.setdefault(char, TrieNode())
                # Add keyword to the output list of the final node
                node.output.append(keyword)

            # Build failure links using BFS
            queue = []
            # Start from root's children
            for node in root.children.values():
                queue.append(node)
                node.fail = root

            # Breadth-first traversal of the trie
            while queue:
                current_node = queue.pop(0)
                # Traverse each child node
                for key, next_node in current_node.children.items():
                    queue.append(next_node)
                    fail_node = current_node.fail
                    # Find the longest proper suffix that is also a prefix
                    while fail_node and key not in fail_node.children:
                        fail_node = fail_node.fail
                    # Set failure link of the current node
                    next_node.fail = fail_node.children[key] if fail_node else root
                    # Add output patterns of failure node to current node's output
                    next_node.output += next_node.fail.output
            return root

        def search_text(text, keywords):
            # Build the Aho-Corasick automaton
            root = build_automaton(keywords)
            # Initialize result dictionary
            # result = {keyword: [] for keyword in keywords}
            result = collections.defaultdict(list)

            current_node = root
            # Traverse the text
            for i, char in enumerate(text):
                # Follow failure links until a match is found
                while current_node and char not in current_node.children:
                    current_node = current_node.fail

                if not current_node:
                    current_node = root
                    continue

                # Move to the next node based on current character
                current_node = current_node.children[char]
                # Record matches found at this position
                for keyword in current_node.output:
                    result[i - len(keyword) + 1].append(keyword)
            return result

        costmp = collections.defaultdict(int)
        for word, c in zip(words,costs):
            if word in costmp:
                costmp[word] = min(costmp[word], c)
            else:
                costmp[word] = c

        words = list(costmp.keys())
        result = search_text(target, words)
        
        n = len(target)

        @cache
        def dp(i):
            if i == n:
                return 0

            tot = inf
            for a in result[i]:
                tot = min(tot, dp(i+len(a)) + costmp[a])

            return tot

        tot = dp(0)
        return -1 if tot == inf else tot
