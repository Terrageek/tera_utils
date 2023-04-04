from tera_utils.src import *

# import random

float_list = sort.make_list(100, float)
int_list = sort.make_list(100, int)

lis = [3.4, 5.7, 10.5, 11, 11.6]


def test_continuate():
    assert sort.bubble_sort(int_list) == sort.merge_sort(int_list)
    assert sort.bubble_sort(float_list) == sort.merge_sort(float_list)


def test_bubble_sort():
    assert sort.bubble_sort(list(range(10, 0, -1))) == list(range(1, 11))
    assert sort.bubble_sort(lis) == [3.4, 5.7, 10.5, 11, 11.6]


def test_merge_sort():
    assert sort.merge_sort(list(range(10, 0, -1))) == list(range(1, 11))
    assert sort.merge_sort(lis) == [3.4, 5.7, 10.5, 11, 11.6]
