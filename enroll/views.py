from django.shortcuts import render
from .models import *

# Create your views here.

def homeEnroll(request):
    #student_data = StudentEnrollment.objects.all()
    #student_data = ProxyStudent.students.get_student_roll_byRange(1004, 1008)
    #student_data = ProxyStudent.students.all()
    student_data = ProxyStudent.students.get_queryset_orderbyid()
    context = {'students': student_data}
    print(student_data)
    return render(request, 'enroll/enroll.html', context)
