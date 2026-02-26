"""
A stack is a linear data structure that follows the
last-in-first-out (LIFO) principle, aka first-in-last-out (FILO).
Both insertion and deletion of data happen at the top of the stack.

Some basic operartions we can do are:
- Push: Add a new element to the stack.
- Pop: Remove and return the top element on the stack.
- Peek: Return the top element on the stack.
- isEmpty: Check if the stack is empty.
- Size: Find the number of elements in the stack.

Stacks can be implemented using arrays, lists, or stacks.
"""


class Stack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, data):
        """
        Add an element to the stack
        """
        self.stack.append(data)
        self.length += 1

    def pushValues(self, array):
        """
        Add multiple values to the stack
        """
        for val in array:
            self.push(val)

    def pop(self, num=1):
        """
        Remove a given number of values
        from the stack and return them
        """
        if num > self.length:
            raise ValueError(
                f"Cannot remove {num} elements from stack of size {self.length}"
            )

        deletedValues = []
        for _ in range(num):
            deletedValues.append(self.stack[-1])
            self.stack.pop()
            self.length -= 1

        return deletedValues

    def peek(self, num=1):
        """
        Return the top elements in the stack
        """
        if num > self.length:
            raise ValueError(f"Length of stack {self.length} is smaller than {num}")

        return self.stack[-num:][::-1]

    def isEmpty(self):
        """
        Check is stack is empty
        """
        return self.length == 0

    def getSize(self):
        """
        Get the length of the stack
        """
        return self.length
