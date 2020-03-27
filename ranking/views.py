from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Student, Marks, Subject, User
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import psycopg2


def student_details(request):
    student = Student.objects.all()
    return render(request, 'ranking/student_details.html', {'student' : student})


# @login_required
def student_mark(request, **kwargs):
    staff_id = kwargs.get("staff_id", None)
    stud_detail = Student.objects.all()
    # subject = Subject.objects.all()
    if request.method == 'POST':
        mark = request.POST.get('mark')
        for stud in stud_detail:
            sub = User.objects.ge()
            mark_obj = Marks.objects.create(sub_name=User.objects.get(pk=staff_id),
                                            stu_name=Student.objects.get(pk=stud.id),
                                            mark=mark)
            mark_obj.save()
    return render(request, 'ranking/student_mark.html', {'stud_detail' : stud_detail})


def total(request, **kwargs):
    stu_obj = Student.objects.all()
    for i in stu_obj:
        print(i.id, "LLLLLLLLLLLLLLLooooooooooooooooooooo")
        total = i.mark + i.mark + i.mark + i.mark + i.mark
    return render(request, 'ranking/total.html', {'total' : total})


def staff_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('ranking:stu_mark'))
    return render(request, 'ranking/user_login.html')
