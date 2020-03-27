from django.urls import path

from . import views

app_name = 'ranking'

urlpatterns = [
	path('student_details/', views.student_details, name='student'),
	path('student_mark/<int:staff_id>/', views.student_mark, name='stu_mark'),
	path('staff_login/', views.staff_login, name='login'),
	path('total/', views.total, name='total')
]
