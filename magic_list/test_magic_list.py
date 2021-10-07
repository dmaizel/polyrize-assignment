from dataclasses import dataclass

import pytest

from magic_list import MagicList


@dataclass
class Person:
    age: int = 1


def test_boundary_check_skip():
    a = MagicList()
    a[0] = 5
    assert a[0] == 5


def test_cls_type():
    a = MagicList(cls_type=Person)
    a[0].age = 5
    assert a == [Person(age=5)]


def test_index_continuity_enforcement():
    a = MagicList(cls_type=Person)
    with pytest.raises(IndexError):
        a[1].age = 5
