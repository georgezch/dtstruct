"""Tests and examples for linked list code"""

from ..linkedlists import LinkedList


def test_init():
    linkedlist = LinkedList()

    assert linkedlist.getLength() == 0
    assert linkedlist.getList() == []

    linkedlist.appendNodeTail(3)
    assert linkedlist.length == 1
    assert linkedlist.getValue(0) == 3
    assert linkedlist.getList() == [3]


def test_get_list():
    linkedlist = LinkedList()

    data = [10, 20, 0, 6, 19]
    linkedlist.initWithValues(data)

    llist = linkedlist.getList()

    assert llist == data

    llist2 = linkedlist.getList(1, 3)
    assert llist2 == data[1:4]


def test_appendNodeTail():
    linkedlist = LinkedList()

    data = [10, 20, 0]
    linkedlist.initWithValues(data)

    linkedlist.appendNodeTail(40)

    assert linkedlist.getLength() == 4
    assert linkedlist.getList() == [10, 20, 0, 40]


def test_appendNodeHead():
    linkedlist = LinkedList()

    data = [10, 20, 0]
    linkedlist.initWithValues(data)

    linkedlist.appendNodeHead(-10)

    assert linkedlist.getLength() == len(data) + 1
    assert linkedlist.getList() == [-10, 10, 20, 0]


def test_get_value():
    linkedlist = LinkedList()

    try:
        linkedlist.getValue(0)
    except ValueError:
        raises_ValueError_NoData = True
    assert raises_ValueError_NoData

    data = [1, 10, -5, 9, 13]
    linkedlist.initWithValues(data)

    try:
        linkedlist.getValue(len(data) + 1)
    except ValueError:
        raises_ValueError_OutOfBouds = True
    assert raises_ValueError_OutOfBouds

    for i, val in enumerate(data):
        assert linkedlist.getValue(i) == val


def test_insertNode():
    linkedlist = LinkedList()

    data = [10, 120, -90]
    linkedlist.initWithValues(data)

    linkedlist.insertNode(1, 20)
    assert linkedlist.getList() == [10, 120, 20, -90]
    assert linkedlist.getLength() == len(data) + 1

    linkedlist.insertNode(2, 15)
    assert linkedlist.getList() == [10, 120, 20, 15, -90]
    assert linkedlist.getLength() == len(data) + 2


def test_deleteNode():
    linkedlist = LinkedList()

    try:
        linkedlist.deleteNode(0)
    except ValueError:
        raises_ValueError_EmptyList = True
    assert raises_ValueError_EmptyList

    linkedlist.appendNodeTail(10)
    linkedlist.deleteNode(0)
    assert linkedlist.getLength() == 0

    linkedlist = LinkedList()
    data = [10, 120, -90]
    linkedlist.initWithValues(data)

    linkedlist.deleteNode(0)
    assert linkedlist.getLength() == len(data) - 1
    assert linkedlist.getList() == [120, -90]

    linkedlist = LinkedList()
    data = [10, 120, -90]
    linkedlist.initWithValues(data)

    linkedlist.deleteNode(1)
    assert linkedlist.getLength() == len(data) - 1
    assert linkedlist.getList() == [10, -90]

    linkedlist = LinkedList()
    data = [4, 10, -1, 40]
    linkedlist.initWithValues(data)

    linkedlist.deleteNode(3)
    assert linkedlist.getList() == [4, 10, -1]
    assert linkedlist.getLength() == len(data) - 1
