# -*- coding: utf-8 -*-
def factiorial(n):
    """
    Args:
        n an int >=1

    Return:
        Factorial of n
    """
    if n== 1:
        return n
    else:
        return n * factiorial(n-1)

print(factiorial(2))
print(factiorial(3))
print(factiorial(1))
print(factiorial(9))
print(factiorial(55))
print(factiorial(958))
