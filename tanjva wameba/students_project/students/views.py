from django.shortcuts import render
import random

def get_random_students():
    names = ['Ana', 'Gio', 'Mariami', 'Sophio', 'Natali', 'Nika']
    surnames = ['Tsiklauri', 'Doladze', 'Bitsadze', 'Beglarishvili', 'Giorgadze', 'Shubladze']

    students = []
    for _ in range(100):
        student = {
            'name': random.choice(names),
            'surname': random.choice(surnames),
            'gpa': round(random.uniform(1.0, 4.0), 2),
            'course': random.randint(1, 4)
        }
        students.append(student)
    return students

def main_page_view(request):
    students = get_random_students()
    random_student = random.choice(students)
    context = {'student': random_student}
    return render(request, 'main_page.html', context=context)

def students_page_view(request):
    students = get_random_students()
    context = {'students': students}
    return render(request, 'students_page.html', context=context)