# You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

# Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:


# Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

# Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].


# Example 1:


# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.
from typing import List


class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]: # type: ignore
      
      if not root:
        return False
      
      self.ans = []
      self.idx = 0
      
      def recurse(node):
        if not node:
          return True
        
        if node.val != voyage[self.idx]:
          return False
        
        self.idx += 1
        if node.left and (node.left.val != voyage[self.idx]):
          if node.right:
            self.ans.append(node.val)
          return recurse(node.right) and recurse(node.left)
        
        else:
          return recurse(node.left) and recurse(node.right)
        
      if recurse(root):
        return self.ans
      return [-1]