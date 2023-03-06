from django.shortcuts import render
from . import models
from .models import StudentNew
from datetime import date, time
from django.db.models import Avg, Max, Min, Sum, Count, Q

# Create your views here.

def home(request):
    #student_data = StudentNew.objects.all()
    #student_data = StudentNew.objects.filter(name__exact='Puja')
    #student_data = StudentNew.objects.filter(name__iexact='sonam')
    #student_data = StudentNew.objects.filter(name__contains='a')
    #student_data = StudentNew.objects.filter(name__icontains='a')
    #student_data = StudentNew.objects.filter(id__in=[1, 2])
    #student_data = StudentNew.objects.filter(marks__in=[50, 60])
    #student_data = StudentNew.objects.filter(marks__gt=50)
    #student_data = StudentNew.objects.filter(marks__gte=50)
    #student_data = StudentNew.objects.filter(marks__lt=70)
    #student_data = StudentNew.objects.filter(marks__lte=50)
    #student_data = StudentNew.objects.filter(name__startswith='s')
    #student_data = StudentNew.objects.filter(name__istartswith='s')
    #student_data = StudentNew.objects.filter(name__endswith='A')
    #student_data = StudentNew.objects.filter(name__iendswith='A')
    #student_data = StudentNew.objects.filter(pass_date__range=('2023-02-01','2023-02-14'))
    #student_data = StudentNew.objects.filter(adm_dateTime_field__date=date(2023,2,10))
    #student_data = StudentNew.objects.filter(adm_dateTime_field__date__gt=date(2023,2,7))
    #student_data = StudentNew.objects.filter(pass_date__year=2023)
    #student_data = StudentNew.objects.filter(pass_date__year__gt=2022)
    #student_data = StudentNew.objects.filter(pass_date__year__gte=2022)
    #student_data = StudentNew.objects.filter(pass_date__month=2)
    #student_data = StudentNew.objects.filter(pass_date__month__gt=1)
    #student_data = StudentNew.objects.filter(pass_date__month__gte=1)
    #student_data = StudentNew.objects.filter(pass_date__month__lte=4)
    #student_data = StudentNew.objects.filter(pass_date__month__lte=4)
    #student_data = StudentNew.objects.filter(pass_date__day__gt=8)
    #student_data = StudentNew.objects.filter(pass_date__day=8)
    #student_data = StudentNew.objects.filter(pass_date__week__lt=7)
    #student_data = StudentNew.objects.filter(pass_date__week_day=4)
    #student_data = StudentNew.objects.filter(pass_date__week_day=4)
    #student_data = StudentNew.objects.filter(pass_date__week_day__gt=4)
    #student_data = StudentNew.objects.filter(pass_date__quarter=1)
    #student_data = StudentNew.objects.filter(adm_dateTime_field__time__gt=time(6,00))
    #student_data = StudentNew.objects.filter(adm_dateTime_field__time__gt=time(21,17))
    #student_data = StudentNew.objects.filter(adm_dateTime_field__hour__gt=5)
    #student_data = StudentNew.objects.filter(adm_dateTime_field__minute__gt=20)
    #student_data = StudentNew.objects.filter(adm_dateTime_field__second__gt=20)
    #student_data = StudentNew.objects.filter(adm_dateTime_field__second=0)
    #student_data = StudentNew.objects.filter(roll__isnull=True)
    #student_data = StudentNew.objects.filter(roll__isnull=False)

    #Aggregate function:--------------------------

    student_data = StudentNew.objects.all()
    avarage = student_data.aggregate(Avg('marks'))
    summation = student_data.aggregate(Sum('marks'))
    howMuch = student_data.aggregate(Count('marks'))
    maximum_marks = student_data.aggregate(Max('marks'))
    minimum_marks = student_data.aggregate(Min('marks'))

    context = {
        'students':student_data,
        'avarage': avarage,
        'summation': summation,
        'howMuch': howMuch,
        'maximum_mark':maximum_marks,
        'minimum_mark': minimum_marks,

    }

    print(student_data)
    print("------------Avarage--------")
    print(avarage)
    print("------sum-------")
    print(summation)
    print("------HowMuch-------")
    print(howMuch)
    print("------maximum_marks-------")
    print(maximum_marks)
    print("------minimum_marks-------")
    print(minimum_marks)
    print("-----------------------")
    print("Query:--", student_data.query)
    return render(request, 'test/index2.html', context)


def q_objects(request):
    #student_data = StudentNew.objects.filter( Q(id=2) & Q(roll=102))
    #student_data = StudentNew.objects.filter( Q(id=3) | Q(roll=102))
    #student_data = StudentNew.objects.filter( ~Q(id=3))# jar id 3 na 3 bade sob
    #student_data = StudentNew.objects.all()[:2]
    #student_data = StudentNew.objects.all()[:10:2]

    print(student_data)
    return render(request, 'test/qobject.html', {'students':student_data})
