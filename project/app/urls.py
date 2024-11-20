from django.urls import path
from . import views

urlpatterns = [
    path('',views.Project_login,name='login'),
    path('logout',views.Project_logout,name='logout'),
    path('register',views.project_registration),
    path('creater_home',views.creater_home),
    path('student_home',views.student_home),
]