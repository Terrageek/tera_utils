from ..src.sort import *

# import random

float_list = make_list(100, float)
int_list = make_list(100, int)

lis = [3.4, 5.7, 10.5, 11, 11.6]


def test_continuate():
    assert bubble_sort(int_list) == merge_sort(int_list)
    assert bubble_sort(float_list) == merge_sort(float_list)


def test_bubble_sort():
    assert bubble_sort(list(range(10, 0, -1))) == list(range(1, 11))
    assert bubble_sort(lis) == [3.4, 5.7, 10.5, 11, 11.6]


def test_merge_sort():
    assert merge_sort(list(range(10, 0, -1))) == list(range(1, 11))
    assert merge_sort(lis) == [3.4, 5.7, 10.5, 11, 11.6]
