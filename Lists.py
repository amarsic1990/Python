listMethods = "https://docs.python.org/2/tutorial/datastructures.html"
import webbrowser
webbrowser.open(listMethods)


string = "Python is cool"
list(string)# list constructor

print(dir(list))


l = string.split()# space default
print(l)


l1 = list()
print(type(l1))


student_names = []
student_names = ["Ante", "Mate", "Marko", "Ivan"]


string = " ".join(l)
print(string)


bbb = "ccc;bbb;vvv"
aaa = bbb.split(";"); print(aaa)


print(student_names[0]); print(student_names[1]); print(student_names[3]); print(student_names[-1])


student_names[0] = "Ivica"
print(student_names[0])


#student_names[4] = "Ana" Error
student_names.append("Ana")
print(student_names[4])


print("Ana" in student_names)
print("Ante" in student_names)
print("Ante" not in student_names)


print(len(student_names))
print(range(len(student_names)))
print(range(len(l)))


print(student_names + l)


del(student_names[2])
print(student_names)


student_names.pop()
print(student_names)


student_names.pop(0)
print(student_names)


student_names.reverse()
print("Reversed students:", student_names)


friends = ["Mate", "Jure", "Ivica", "Ana", "Ivana"]; print(friends)
friends.sort(); print(friends)


friends = ["Mate", "Jure", "Ivica", "Ana", "Ivana"]; print(friends)
friends_reversed = reversed(friends)
print("friends_reversed", friends_reversed)# <list_reverseiterator object at 0x0000018A59E1C978>
print([i for i in friends_reversed])


friends_sorted = sorted(friends)
print("friends_sorted", friends_sorted)


friends = ["Mate", "Jure", "Ivica", "Ana", "Ivana"]
friends.extend(range(len(friends))); print("friends extended", friends)
print(friends)
friends.extend([i for i in range(15,25)])
print(friends)
l = ["a", "b", "c"]
friends.extend(l)
print(friends)
friends.extend(["Canopy", "Monty"])
print(friends)


friends.remove("Ana")
print(friends)
friends.index("Jure")


l = list()
l.insert(0, "P")
l.insert(1, "y")
l.insert(2, "t")
l.insert(3, "h")
l.insert(4, "o")
l.insert(5, "n")


print(l)

del l[0]; print(l)


n = [99,32,21,12]
print(max(n))
print(min(n))
print(len(n))
print(sum(n))
print(sum(n)/len(n))


friends = ["Mate", "Jure", "Ivica", "Ana", "Ivana"]; print(friends)
for f in friends:
    print(f)


print([f for f in friends])


#List Slicing:
student_names = ["Ante", "Mate", "Marko", "Ivan"]
print(student_names[1:])
print(student_names[1:-1])
print(student_names[:])
print(student_names[:-1])
print(student_names[::2])
print(student_names[::-1])
