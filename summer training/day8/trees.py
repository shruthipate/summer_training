#inorder
'''class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    
    def traverse(node):
        if node is not None:
            traverse(node.left)        # Visit left subtree
            result.append(node.value)  # Visit root
            traverse(node.right)       # Visit right subtree

    traverse(root)
    return result

# Example usage:
# Constructing the following binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

# Creating tree nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Performing inorder traversal
print(inorder_traversal(root))  # Output: [4, 2, 5, 1, 3]'''




class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    
    return root

def preorder_traversal(root):
    result = []
    
    def traverse(node):
        if node is not None:
            result.append(node.value)  # Visit root
            traverse(node.left)        # Visit left subtree
            traverse(node.right)       # Visit right subtree

    traverse(root)
    return result

# Example usage:
# Constructing the BST by inserting values

values = [10, 5, 15, 3, 7, 13, 18]
root = None
for value in values:
    root = insert_into_bst(root, value)

# Performing preorder traversal to print the BST
print(preorder_traversal(root))  # Output: [10, 5, 3, 7, 15, 13, 18]
