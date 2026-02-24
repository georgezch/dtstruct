"""Tests and examples for linked list code"""

from ..linkedlists import LinkedList


def test_init():
    linedlist = LinkedList()

    assert linedlist.getLength() == 0
    assert linedlist.getList() == []
