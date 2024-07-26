from django.shortcuts import render, get_object_or_404, redirect
from .models import Student

def index(request):
    return render(request, 'students/index.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
        student = Student(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            date_of_birth=request.POST['date_of_birth'],
            enrollment_date=request.POST['e']
        )
        student.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html')

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.email = request.POST['email']
        student.date_of_birth = request.POST['date_of_birth']
        student.enrollment_date = request.POST['enrollment_date']
        student.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
