








class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 从数组构建二叉树
def buildTree(vals, layer = 0, pos = 0):
    if layer <= 0:
        val_pos = 0
    else:
        val_pos = 2**layer - 1 + pos

    if len(vals) <= val_pos or vals[val_pos] == None:
        return
    root = TreeNode(vals[val_pos])
    root.left = buildTree(vals, layer + 1, 2 * pos)
    root.right = buildTree(vals, layer + 1, 2 * pos + 1)
    return root