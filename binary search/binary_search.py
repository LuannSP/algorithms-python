from typing import Any


def binary_search(array: Any, elem: Any, begin: int = 0, end: int = None) -> (int | Any | None):
    if end is None:
        end = len(array)-1
    if begin <= end:
        half = (begin + end)//2
        if array[half] == elem:
            return half
        if elem < array[half]:
            return binary_search(array, elem, begin, half-1)
        else:
            return binary_search(array, elem, half+1, end)
    return None
