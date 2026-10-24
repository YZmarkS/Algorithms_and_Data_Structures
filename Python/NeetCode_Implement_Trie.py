class Node:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            c_index = ord(c) - ord('a')
            if curr_node.children[c_index] is None:
                curr_node.children[c_index] = Node()
            curr_node = curr_node.children[c_index]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            c_index = ord(c) - ord('a')
            if curr_node.children[c_index] is None:
                return False
            curr_node = curr_node.children[c_index]
        return curr_node.is_end

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in word:
            c_index = ord(c) - ord('a')
            if curr_node.children[c_index] is None:
                return False
            curr_node = curr_node.children[c_index]
        return True
