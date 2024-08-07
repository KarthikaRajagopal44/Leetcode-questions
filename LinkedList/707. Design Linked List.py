# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
 
class MyLinkedList:
    class _Node:
        def __init__(self, val=None, prev=None, next=None):
            self._val = val
            self._prev = prev
            self._next = next

        def __str__(self):
            return f"{self._val}"

        def __repr__(self):
            return f"{self._val}"

    def __init__(self):
        self._head = self._Node(None)
        self._tail = self._Node(None)
        self._size = 0
        self._head._next = self._tail
        self._tail._prev = self._head

    def _getAtIndex(self, index) -> "_Node":
        curr = None
        if index == self._size-1:
            return self._tail._prev
        elif index == 0:
            return self._head._next
        if self._size - index < index:
            curr = self._tail._prev

            i = self._size - 1
            while i > index:

                curr = curr._prev
                i -= 1

        else:
            curr = self._head._next
            i = 0
            while i < index:
                curr = curr._next
                i += 1
        return curr

    def _insert_between(self, e, prev, succ) -> None:
        n = self._Node(e, prev, succ)
        prev._next = n
        succ._prev = n
        self._size += 1

    def get(self, index: int) -> int:
        if index >= self._size or self._size == 0:
            return -1
        curr = self._getAtIndex(index)
        return curr._val

    def addAtHead(self, val: int) -> None:
        self._insert_between(val, self._head, self._head._next)

    def addAtTail(self, val: int) -> None:
        self._insert_between(val, self._tail._prev, self._tail)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self._size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self._size :
            self.addAtTail(val)
        else: 
            curr = self._getAtIndex(index)
            self._insert_between(val, curr._prev, curr)

    def deleteAtIndex(self, index: int) -> None:
        
        if 0<=index < self._size:
            curr = self._getAtIndex(index)
            curr._prev._next = curr._next
            curr._next._prev = curr._prev
            self._size -= 1
            curr = None


# https://leetcode.com/problems/design-linked-list/solutions/4481750/doubly-linked-list-solution-with-python