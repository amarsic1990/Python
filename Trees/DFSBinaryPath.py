# -*- coding: utf-8 -*-
from binaryTreeBetter import *

def DFS_binary_path(root, fcn):
    
    stack = [root]
    while(len(stack)) > 0:
        if fcn(stack[0]):
            return trace_path(stack[0])
        else:
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
    return False

def trace_path(node):
    if not node.get_parent():
        return [node]
    else:
        return [node] + trace_path(node.get_parent())


def print_path(tree):
    
    print([i.get_value() for i in tree])


def find6(obj):
    return obj.get_value() == 6 


def find1(obj):
    return obj.get_value() == 1


def find2(obj):
    return obj.get_value() == 2 


def find3(obj):
    return obj.get_value() == 3  


def find10(obj):
    return obj.get_value() == 10 


foo = DFS_binary_path(n5, find6)
print_path(foo)       