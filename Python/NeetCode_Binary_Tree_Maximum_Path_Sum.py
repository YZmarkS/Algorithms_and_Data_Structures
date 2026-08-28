class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: Optional[TreeNode]) -> int:

    def helper(root: Optional[TreeNode]):
        best_rooted = None
        best_isolated = None
        if root.left is None and root.right is None:
            best_rooted = root.val,
            best_isolated = root.val
        elif root.left is not None and root.right is None:
            sub_best_rooted, sub_best_isolated = helper(root.left)
            best_rooted = max(0, sub_best_rooted) + root.val
            best_isolated = max(sub_best_isolated, best_rooted)
        elif root.right is not None and root.left is None:
            sub_best_rooted, sub_best_isolated = helper(root.right)
            best_rooted = max(0, sub_best_rooted) + root.val
            best_isolated = max(sub_best_isolated, best_rooted)
        else: # Both children non-empty
            (best_left_rooted, best_left_isolated) = helper(root.left)
            (best_right_rooted, best_right_isolated) = helper(root.right)
            best_rooted = max(0, best_left_rooted, best_right_rooted) + root.val
            best_isolated = max(best_rooted, \
                                best_left_isolated,
                                best_right_isolated)

        return (best_rooted, best_isolated)

    return max(helper(root))
