# -*- coding: utf-8 -*-
from urllib.request import urlopen

student = {"name": "Jure",
            "student_id":212,
            "feedback": None
            }

# List of Dictionaries
all_students = [
                {"name": "Jure", "student_id": 212},
                {"name": "Maja", "student_id": 213},
                {"name": "Ivana", "student_id": 214}
]

print(student["name"])
print(student["student_id"])
print(student["feedback"])

#print(student["last_name"])# KeyError
print(student.get("last_name", "Unknown"))

student["student_id"] = student.get("student_id", 0) + 100
print(student["student_id"])

print(student.keys())
print(student.values())
print(student.items())

del student["feedback"]
print(student.keys())
del student["name"]
print(student)

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words_dict = {}
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words_dict[word] = story_words_dict.get(word,0)+1
            
print(story_words_dict)
print(story_words_dict["it"])