from django.shortcuts import render, HttpResponse
import random

# Create your views here.

# def index(request):
#   return HttpResponse("Hello Geeks")

from django.shortcuts import render
import random

def create_groups(request):
    if request.method == 'POST':
        students_input = request.POST.get('students', '')  # Obtener los nombres de los estudiantes del formulario
        students = [name.strip() for name in students_input.split(',') if name.strip()]  # Convertir la entrada en una lista de nombres de estudiantes
        random.shuffle(students)
        groups = []

        while len(students) >= 2:
            group = students[:2]
            groups.append(group)
            students = students[2:]

        remaining_students = len(students)
        ungrouped_student = students[0] if remaining_students % 2 else None
        print(groups)
        print(ungrouped_student)

        return render(request, 'Grupos/create_groups.html', {'groups': groups, 'ungrouped_student': ungrouped_student})
    
    return render(request, 'Grupos/create_groups.html')