"""
Implementation of Linked Lists in Python.
A likned list is a data structure that consists of nodes,
which are blocks of some sort of data, and a pointer, or link,
that points to the next node.

Compared to arrays, which are linear data structures that have some
fixed length and stores data right after each other, linked lists:
- Do not have a fixed size
- Elements, or nodes, are not stored next to each other
- Have higher memory demands
- A node cannot be accessed directly, but the list has to be traversed
- Nodes can be inserted of delected in linear time, without shifting in memory

There a various types of linked lists:
- Singly linked: each node has only one link to the next node
- Doubly linked: each node has links to both the next and previous nodes
- Circular linked: singly or doubly lined with the head and tail also linked

Linked list operations:
- Traversal: go through list by following links from node to node
- Removal of node: remove a node and connet nodes on each side of deleted node
- Insertion of node: add node and properly connect nodes to not break the list
- Sorting: finding largest or lowest value in the list

Time complexity:
- Traversing is an O(n) operation, like arrays
- Deleting and removing is O(1), better than arrays which are O(n)
"""


class Node:
    """
    Node is the storage unit, which contains some
    data and a pointer to the next node.
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    The linked list, essentially a wrapper around the
    `Node` class to perform various operations
    """

    def __init__(self):
        self.head = Node()

    def appendNode(self, data):
        """
        Adding a node at the end of the list
        """
        newNode = Node(data)
        curr = self.head
        while curr is not None:
            curr = curr.next
        curr.next = newNode

    def getLength(self):
        """
        Get the length of the list
        """
        curr = self.head
        tot = 0
        while curr.next is not None:
            tot += 1
            curr = curr.next

        return tot

    def getList(self):
        """
        Collect all elements from all nodes and return as list
        """
        elms = []
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            elms.append(curr.data)

        return elms

    def displayList(self):
        """
        Print all elements from all nodes
        """
        print(self.getList())

    def getValue(self, index):
        """
        Get value of node by index
        """
        length = self.getLength()
        if index > length:
            raise Exception(
                f"!ERROR! Index {index} out of range for list of length {length}"
            )

        curr = self.head
        i = 0
        while curr.next is not None and i < index:
            curr = curr.next
            i += 1

        return curr.data
