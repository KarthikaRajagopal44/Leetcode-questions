# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Helper function to perform DFS and backtrack
    def dfs(self, root, path, ans, remainingSum):
        # If the current node is None, return as there's nothing to process
        if not root:
            return
        
        # Add the current node's value to the ongoing path
        path.append(root.val)
        
        # Check if the current node is a leaf (no left or right child)
        # and if the remaining sum equals the current node's value
        if not root.left and not root.right and remainingSum == root.val:
            # If it's a valid path, add a copy of the current path to the results
            ans.append(list(path))
        
        # Continue the DFS on the left subtree with the updated remaining sum
        self.dfs(root.left, path, ans, remainingSum - root.val)
        
        # Continue the DFS on the right subtree with the updated remaining sum
        self.dfs(root.right, path, ans, remainingSum - root.val)
        
        # Backtrack by removing the last node added to the path
        # This allows us to explore a new path
        path.pop()
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]: # type: ignore
        # Initialize the list to store all valid paths
        ans = []
        # Start the DFS from the root with an empty path and the target sum
        self.dfs(root, [], ans, targetSum)
        # Return the list of valid paths
        return ans
