from typing import List

def sum_(a: int, b: int) -> int:
    return a+b

def list_sum(a: List, b: List) -> List:
    return [i+j for i, j in zip(a,b)]

def substract(a: int, b: int) -> int:
    return a-b

def list_substract(a: List, b: List) -> List:
    return [i-j for i, j in zip(a,b)]


def is_num(a):
    if isinstance(a, int):
        return True
    return False
