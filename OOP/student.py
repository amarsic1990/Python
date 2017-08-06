# -*- coding: utf-8 -*-
class Student(object):
    school_name = "FER"
    students = []
    
    
    def __init__(self, name, student_id = 999):
        self.name = name
        self.student_id = student_id
        Student.students.append(self)
        
    
    def __str__(self):
        return "Student " + self.name
        
        
    def get_name_capitalize(self):
        return self.name.capitalize()
        
        
    def get_school_name(self):
        return self.school_name