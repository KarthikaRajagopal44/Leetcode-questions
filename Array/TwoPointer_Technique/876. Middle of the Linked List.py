# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.


from typing import List

#   List means ListNode
class Solution:
     def middleNode(self, head: List) -> List:            
        slow = head
        fast = head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next

        return slow



# link  to solution approach:
# https://leetcode.com/problems/middle-of-the-linked-list/solutions/4834674/iterative-and-recursive-slow-fast
        