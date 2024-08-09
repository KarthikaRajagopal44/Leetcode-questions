# Binary Tree:

# A binary tree is a tree data structure where each node has at most two children, referred to as the left child and the right child. Binary trees are fundamental in computer science and are used in various applications like searching, sorting, and data storage.

# Basics of a Binary Tree:
# Node: A single element in the tree that contains data and pointers to its left and right children.
# Root: The topmost node in a binary tree.
# Leaf: A node with no children.
# Subtree: A tree formed by any node and its descendants.
# Height: The length of the longest path from the root to a leaf.
# Depth: The distance from the root to a particular node.
# Binary Tree Structure:
# Each node in a binary tree has:

# Data: The value stored in the node.
# Left Child: A pointer/reference to the left child node.
# Right Child: A pointer/reference to the right child node.

# Binary Search Tree:

# A Binary Search Tree (BST) is a special type of binary tree that satisfies the following properties:

# Left Subtree: All the nodes in the left subtree of a node have values less than the node's value.
# Right Subtree: All the nodes in the right subtree of a node have values greater than the node's value.
# No Duplicates: Typically, BSTs do not allow duplicate values.
# Differences Between Binary Tree and Binary Search Tree:
# Structure:
# Binary Tree: No specific order in how nodes are arranged.
# BST: Nodes are arranged in a specific order (left child < parent < right child).
# Searching:
# Binary Tree: Requires traversal of all nodes (O(n)).
# BST: Allows efficient searching (O(log n)) by leveraging its ordering properties.