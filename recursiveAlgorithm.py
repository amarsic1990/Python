# -*- coding: utf-8 -*-
def fibonacci(x):
    """Calculates Fibonacci of x

    Args:
        x an int >=0

    Returns:
        Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


print(fibonacci(1))
print(fibonacci(0))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(20))
print(fibonacci(30))
print(fibonacci(40))


def find_elem_recur(e, L):
    """ Assumption L is sorted
    Args:
        e int
        L list

    Returns:
        True if e is in list False otherwise
    """
    if len(L) == 0:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return find_elem_recur(e, L[:half])
        else:
            return find_elem_recur(e, L[half:])


print(find_elem_recur(1, [1, 2, 3, 5, 7, 8, 9, 15]))
print(find_elem_recur(15, [1, 2, 3, 5, 7, 8, 9, 15]))
print(find_elem_recur(150, [1, 2, 3, 5, 7, 8, 9, 15]))
print(find_elem_recur(4, [1, 2, 3, 5, 7, 8, 9, 15,4]))
print(find_elem_recur(15, [1, 2, 3, 4, 5, 7, 8, 9, 15]))


def is_palindrome(s):
    """
    Args:
        s string

    Returns:
        True if word is palindrome False otherwise
    """
    def to_chars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))


print(is_palindrome("ante"))
print(is_palindrome("anna"))
print(is_palindrome("Able was I, ere I saw Elba"))
