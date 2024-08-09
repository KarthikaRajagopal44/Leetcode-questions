# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: # type: ignore
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            # Append current node's value to the path
            path.append(str(node.val))
            
            # If it's a leaf node, add the path to result
            if not node.left and not node.right:
                res.append('->'.join(path))
            else:
                # Continue to search in left and right subtrees
                dfs(node.left, path)
                dfs(node.right, path)
            
            # Backtrack: remove the current node's value from the path
            path.pop()
        
        # Initialize the DFS with an empty path
        dfs(root, [])
        
        return res