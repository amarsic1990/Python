# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:03:58 2017

@author: marsic
"""

class Binary_tree(object):
    
    
    def __init__(self, value):
        self.value = value
        self.left_branch = None
        self.right_branch = None
        self.parent = None
        
        
    def set_left_branch(self, node):
        self.left_branch = node
        
        
    def set_right_branch(self, node):
        self.right_branch = node
        
        
    def set_parent(self, parent):
        self.parent = parent
        
        
    def get_value(self):
        return self.value
    
    
    def get_left_branch(self):
        return self.left_branch
    
    
    def get_right_branch(self):
        return self.right_branch
    
    
    def get_parent(self):
        return self.parent
    
    
    def __str__(self):
        return str(self.value)

    
n5 = Binary_tree(5)
n2 = Binary_tree(2)
n1 = Binary_tree(1)
n4 = Binary_tree(4)
n8 = Binary_tree(8)
n6 = Binary_tree(6)
n7 = Binary_tree(7)

n5.set_left_branch(n2)
n2.set_parent(n5)
n5.set_right_branch(n8)
n8.set_parent(n5)
n2.set_left_branch(n1)
n1.set_parent(n2)
n2.set_right_branch(n4)
n4.set_parent(n2)
n8.set_left_branch(n6)
n6.set_parent(n8)
n6.set_left_branch(n7)
n7.set_parent(n6)

print(n5.get_parent())
print(n2.get_parent())
print(n1.get_parent())
print(n4.get_parent())
print(n8.get_parent())
print(n6.get_parent())
print(n7.get_parent())