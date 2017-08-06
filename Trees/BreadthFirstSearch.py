# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:11:59 2017

@author: marsic
"""

from binaryTreeBetter import *

def breadth_first_search_binary(root, fcn):
    
    queue = [root]
    while len(queue) > 0:
        print("at node " + str(queue[0].get_value()))
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.get_left_branch():
                queue.append(temp.get_left_branch())
            if temp.get_right_branch():
                queue.append(temp.get_right_branch())
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
  
breadth_first_search_binary(n5, find6)
breadth_first_search_binary(n5, find2)
breadth_first_search_binary(n5, find10)
    