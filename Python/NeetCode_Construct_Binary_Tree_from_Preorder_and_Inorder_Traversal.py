class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    length = len(preorder)
    if length == 0:
        return None

    nodes = [ TreeNode() for _ in range(length) ]
    stack = []
    i, j = 0, 0
    while i < length and j < length:
        last = None
        # Keep go left
        while preorder[i] != inorder[j]:
            nodes[i].val = preorder[i]
            if last is not None:
                last.left = nodes[i]
            last = nodes[i]
            stack.append((preorder[i], i))
            i += 1

        print("Gone left")
        print(i, j, stack)

        nodes[i].val = preorder[i]
        if last is not None:
            last.left = nodes[i]
        stack.append((preorder[i], i))
        i += 1

        print("Left most")
        print(i, j, stack)

        critical = None
        while stack and stack[-1][0] == inorder[j]:
            print("here")
            critical = stack[-1][1]
            stack.pop()
            j += 1

        print("Gone back")
        print(i, j, stack)

        if i < length:
            nodes[critical].right = nodes[i]

    return nodes[0]
