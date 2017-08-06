# -*- coding: utf-8 -*-
def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n") 
        f.close()
    except Exception:
        print("Could not save file")

        
save_file("Ivan")
save_file("Jure")
save_file("Božo")        
save_file("Ana")        
save_file("Ivana")
save_file("Maja")


def save_file1(student):
    try:
        f = open("students.txt", "w")
        f.write(student + "\n") 
        f.close()
    except Exception:
        print("Could not save file")
        
save_file1("Irena")


save_file("Ivan")
save_file("Jure")
save_file("Božo")        
save_file("Ana")        
save_file("Ivana")
save_file("Maja")


students = ["Ivan", "Jure", "Božo", "Ana", "Ivana", "Maja"]


def save_file2(student):
    try:
        f = open("students2.txt", "a")
        for i in student:
            f.write(i + "\n") 
        f.close()
    except Exception:
        print("Could not save file")
        
save_file2(students)


students = [{"name": "Ivan", "age":15}, {"name":"Jure", "age":23}, {"name":"Božo", "age":37}, {"name": "Ana", "age":24}, {"name":"Ivana", "age":29}, {"name":"Maja", "age":27}]


def save_file3(student):
    try:
        f = open("students3.txt", "a")
        for i in range(len(students)):
            f.write(students[i]["name"] + " --> " + str(students[i]["age"]) + "\n") 
        f.close()
    except Exception:
        print("Could not save file")
        
        
save_file3(students)



students = [{"name": "Ivan", "age":15}, {"name":"Jure", "age":23}, {"name":"Božo", "age":37}, {"name": "Ana", "age":24}, {"name":"Ivana", "age":29}, {"name":"Maja", "age":27}]


def save_file4(student, txtfile):
    try:
        f = open(txtfile, "a")
        for i in range(len(students)):
            f.write(students[i]["name"] + " --> " + str(students[i]["age"]) + "\n") 
        f.close()
    except Exception:
        print("Could not save file")
        
save_file4(students, "abcd.txt")