# -*- coding: utf-8 -*-
from binaryTreeBetter import *


def depth_first_search_binary(root, fcn):
    stack = [root]
    while len(stack) > 0:
        print("at node " + str(stack[0].get_value()))
        if fcn(stack[0]):
            return True
        
        else:
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
    return False


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
  
depth_first_search_binary(n5, find6)
depth_first_search_binary(n5, find2)
depth_first_search_binary(n5, find10)