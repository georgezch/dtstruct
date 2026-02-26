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

Linked lists can be used for:
- Stacks and Queues (FIFO and LIFO structures) where
  elements are added and removed efficiently from the ends.
- Graphs (specifically, the adjacency list representation) and
  Trees (like binary search trees).
- Hash Tables to handle collisions using a technique called chaining.
- Browser history: Doubly linked lists allow users to navigate back and forward
  through visited web pages efficiently.
- Music/video playlists: Playlists often use circular or doubly linked lists
  to manage song order and loop playback.
- Undo/Redo functionality: Text editors and design software use doubly
  linked lists to store a history of actions,
  allowing easy navigation between states.
- The Linux kernel uses linked lists for various internal data
  management tasks, such as managing active processes.
- Resource scheduling algorithms, like Round Robin, often use
  circular linked lists to ensure fair allocation of CPU time to processes.
- File systems can use linked lists (e.g., the FAT system) to
  manage non-contiguous disk storage for files.
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
        self.head = None
        self.length = 0

    def appendNodeTail(self, data):
        """
        Adding a node at the end of the list
        """
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode
        self.length += 1

    def initWithValues(self, data):
        for val in data:
            self.appendNodeTail(val)

    def appendNodeHead(self, data):
        """
        Adding a node at the beginning of the list
        """
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def getLength(self):
        """
        Get the length of the list
        """
        return self.length

    def getList(self, startind=0, endind=None):
        """
        Collect all elements from all nodes and return as list
        """
        if self.head is None:
            return []

        if endind is None:
            endind = self.length

        cur = self.head
        if startind == 0:
            elms = [self.head.data]
        else:
            elms = []

        i = 1
        while cur.next is not None:
            cur = cur.next

            if i >= startind and i <= endind:
                elms.append(cur.data)

            i += 1
            if i > endind:
                break

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
        if index > self.length:
            raise ValueError(
                f"Index {index} out of range for list of length {self.length}"
            )

        if self.head is None:
            raise ValueError("List contains no data")

        if index == 0:
            return self.head.data

        cur = self.head
        i = 0
        while cur.next is not None:
            cur = cur.next

            i += 1
            if i == index:
                break

        return cur.data

    def insertNode(self, index, data):
        """
        Insert a node to the right of a specific place by index
        """
        if self.head is None or self.length == 1:
            self.appendNodeTail(data)
            self.length += 1
            return

        newNode = Node(data)

        cur = self.head
        i = 0
        while cur.next is not None:
            cur = cur.next

            i += 1
            if i == index:
                break

        newNext = cur.next
        cur.next = newNode
        cur.next.next = newNext

        self.length += 1

    def deleteNode(self, index):
        """
        Delete a node by index
        """
        if self.head is None:
            raise ValueError("Cannot delete from empty list")

        if index >= self.length:
            raise ValueError(
                f"Out of bounds index {index} of list with length {self.length}"
            )

        if self.length == 1:
            self.head = None
            self.length = 0
            return

        if index == 0:
            newHead = self.head.next
            self.head = newHead
            self.length -= 1
            return

        cur = self.head
        i = 0
        while cur.next is not None:
            if index == i + 1:
                break
            i += 1

            cur = cur.next

        if cur.next.next is None:
            cur.next = None
            self.length -= 1
            return

        newNext = cur.next.next
        cur.next = newNext
        self.length -= 1

        return
