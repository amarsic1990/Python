def read_file():
    try:
        f = open("students.txt" ,"r")
        for s in f.readlines(): print(s)
        f.close()
    except:
        print("Could not read file!")
        
        
read_file()



def read_file1(txtfile):
    try:
        f = open(txtfile ,"r")
        for s in f.readlines(): print(s)
        f.close()
    except:
        print("Could not read file!")
        

read_file1("students3.txt")