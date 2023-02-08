from ..my_sort import *

float_list = [10.5, 11.6, 3.4, 5.7, 11]


def test_bubble():
    assert bubble_sort(list(range(10,0,-1))) == list(range(1, 11))
    assert bubble_sort(float_list) == [3.4, 5.7, 10.5, 11, 11.6]