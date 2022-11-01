import re

students, new_list = [], []
group = input("Write your group: ")
tmp = input("Write list of students: \n")

while tmp:
    students.append(tmp.strip())
    tmp = input()

for i in range(len(students)):
    try:
        tmp, surname, name, dot1, midname, dot2, gr, tmr = re.split(r"(\w+\D\w+)\s+(\w)([.])(\w)([.])\s+(.+)", students[i])
        if name != midname or gr != group:
            print(surname, ' ', name, '.', midname, '. ', gr, sep = '')
    except ValueError:   #случай неправильного ввода списка (в том числе и отсутсвие точек после инициалов)
        print("Format of the name is incorrect: ", students[i])
