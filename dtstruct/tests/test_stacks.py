"""Tests and examples for stacks code"""

from ..stacks import Stack


def test_push():

    stack = Stack()

    assert stack.getSize() == 0

    stack.push(10)
    assert stack.getSize() == 1

    stack.pushValues([1, 2, 3, 4])
    assert stack.getSize() == 5


def test_peek():
    stack = Stack()

    data = [1, 2, 3, 4]
    stack.pushValues(data)
    assert stack.getSize() == len(data)

    peek = stack.peek()
    assert peek == [data[-1]]

    peek = stack.peek(3)
    assert peek == [4, 3, 2]

    try:
        stack.peek(10)
    except ValueError:
        raises_ValueError_outOfBounds = True
    assert raises_ValueError_outOfBounds


def test_pop():

    stack = Stack()

    data = [1, 2, 3, 4]
    stack.pushValues(data)
    assert stack.getSize() == len(data)
    assert stack.peek() == [4]

    stack.pop()
    assert stack.getSize() == len(data) - 1
    assert stack.peek() == [3]

    try:
        stack.pop(10)
    except ValueError:
        raises_ValueError_outOfBounds = True
    assert raises_ValueError_outOfBounds


def test_isEmpty():

    stack = Stack()
    assert stack.isEmpty()

    data = [1, 2, 3, 4]
    stack.pushValues(data)
    assert not stack.isEmpty()


def test_getSize():

    stack = Stack()
    assert stack.getSize() == 0

    data = [1, 2, 3, 4]
    stack.pushValues(data)
    assert stack.getSize() == len(data)
