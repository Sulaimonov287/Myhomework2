from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import Students
from .forms import StudentForm


def show_students(request):
    students = Students.objects.all()
    return render(request, 'students.html', context={'students':students})


def create_students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('students')

    else:
        form = StudentForm()

    return render(request, 'students_create.html', context={'form':form})



def update_students(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('students')

    else:
        form = StudentForm(instance=student)

    return render(request, 'students_update.html', context={'form':form, 'student':student})



def delete_students(request, pk):
    student = get_object_or_404(Students, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('students')

    return render(request, 'students_delete.html', context={'student':student})