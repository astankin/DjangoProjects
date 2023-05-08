from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import StudentForm
from .models import Student


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'students': Student.objects.all()
    })


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'view_student.html', {
        'student': student
    })


def search_student(request):
    if request.method == "POST":
        searched = request.POST['searched']
        students = Student.objects.filter(first_name__contains=searched)
        return render(request, 'search_student.html',
                      {'searched': searched,
                       'students': students})
    else:
        return render(request, 'search_student.html',
                      {})


def all_students(request):
    return render(request, 'all_students.html', {
        'students': Student.objects.all()
    })


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa
            )
            new_student.save()
            return render(request, 'add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'add.html', context=context)


def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {
        'form': form
    })


def delete(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        return render(request, 'delete.html', {
            'student': student,
            'success': True
        })
    else:
        return render(request, 'delete.html', {
            'student': student
        })
