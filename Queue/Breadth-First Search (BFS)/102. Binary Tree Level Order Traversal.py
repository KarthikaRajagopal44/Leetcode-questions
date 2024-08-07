# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        if not root:
            return []
        
        ans = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            level = []
            
            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(level)
        
        return ans
    
    # https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/5394346/best-approach-is-here-beats-100