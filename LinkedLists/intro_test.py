import pytest
from intro import LinkedList


def test_init():
    ll = LinkedList(1)
    assert ll.head is not None
    assert ll.tail is not None
    assert ll.head.value == 1
    assert ll.tail.value == 1
    assert ll.length == 1


def test_append_and_tail():
    ll = LinkedList(1)
    ll.append(2)
    assert ll.length == 2
    assert ll.tail.value == 2
    assert ll.head.next.value == 2


def test_pop_single_and_empty():
    ll = LinkedList(42)
    val = ll.pop()
    assert val == 42
    assert ll.head is None
    assert ll.tail is None
    assert ll.length == 0
    # popping empty returns None
    assert ll.pop() is None


def test_pop_multiple():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    assert ll.length == 3
    val = ll.pop()
    assert val == 3
    assert ll.length == 2
    assert ll.tail.value == 2


def test_pop_clean_empty_and_single():
    ll = LinkedList(100)
    # pop_clean on non-empty single should return value and make list empty
    v = ll.pop_clean()
    assert v == 100
    assert ll.length == 0
    assert ll.head is None and ll.tail is None
    # pop_clean on empty returns None
    assert ll.pop_clean() is None


def test_prepend_after_empty_and_nonempty():
    ll = LinkedList(5)
    ll.pop()
    assert ll.length == 0
    ll.prepend(10)
    assert ll.length == 1
    assert ll.head.value == 10
    assert ll.tail.value == 10

    ll.prepend(20)
    assert ll.length == 2
    assert ll.head.value == 20
    assert ll.head.next.value == 10


def test_pop_first_behaviour():
    ll = LinkedList(7)
    ll.append(8)
    x = ll.pop_first()
    assert x == 7
    assert ll.length == 1
    assert ll.head.value == 8
    # pop_first until empty
    assert ll.pop_first() == 8
    assert ll.pop_first() is None


def test_print_list_output(capsys):
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.print_list()
    captured = capsys.readouterr()
    out = captured.out
    assert "The new list is" in out
    assert "End of list" in out
    assert "1" in out
    assert "2" in out
    assert "3" in out
