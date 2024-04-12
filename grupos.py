import random
students = []

while True:
    student = input("Ingrese estudiante, 0 para salir: ")
    if student !="0":
        students.append(student)
        print(students)
    else:
        break

random.shuffle(students)

while len(students) >=2:
    gruops = students[:2]
    print(gruops)
    students = students[2:]
    
if len(students) %2:
    print(f'el alumno: {students[0]} no tiene grupo')

