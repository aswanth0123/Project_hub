from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def Project_login(request):
    if 'creater' in request.session:
        return redirect(creater_home)
    if 'student' in request.session:
        return redirect(student_home)
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        data = authenticate(username=uname,password=pwd)
        if data is not None:
            login(request,data)
            if data.is_staff and not(data.is_superuser):
                request.session['creater'] = uname
                return redirect(creater_home)
            elif data.is_staff==False and not(data.is_superuser):
                request.session['student'] = uname
                return redirect(student_home)               

    else:
        return render(request,'login.html')

def project_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        role = request.POST['role']
        print(role)
        if role == 'creater':
            data=User.objects.create_user(first_name=name,email=email,password=pwd,username=email,is_staff=True)
            data.save()
        else:
            data=User.objects.create_user(first_name=name,email=email,password=pwd,username=email)
            data.save()
        return redirect(Project_login)
    return render(request,'registration.html')

def Project_logout(req):
    logout(req)
    req.session.flush()
    return redirect(Project_login)

@login_required
def creater_home(request):
    return render(request,'creater/home.html')

@login_required
def student_home(request):
    return render(request,'student/home.html')