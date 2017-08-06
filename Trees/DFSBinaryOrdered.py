# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:49:18 2017

@author: marsic
"""

from binaryTreeBetter import *


def DFS_binary_ordered(root, fcn, lt_fcn):
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return True
        elif lt_fcn(queue[0]):
            temp = queue.pop(0)
            if temp.get_left_branch():
                queue.insert(0,temp.get_left_branch())
        else:
            temp = queue.pop(0)
            if temp.get_right_branch():
                queue.insert(0, temp.get_right_branch())
                
    return False


def lt6(node):
    return node.get_value() > 6


def find6(obj):
    return obj.get_value() == 6 

DFS_binary_ordered(n5, find6, lt6)