from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from course.students import add_student
from tool.user import add_user_login, change_password, find_user_login
from views.mybook import page_settings


def redirect_register(**kwargs):
    return redirect(f'/course/{kwargs.get("course")}/register')


def redirect_login(**kwargs):
    return redirect(f'/course/{kwargs.get("course")}/login')


def student_register(request, **kwargs):
    course = kwargs.get("course")

    if request.method == 'POST':

        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:

            # Add new user
            u = find_user_login(email)
            if not u:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That username is taken')
                    return redirect_register(**kwargs)
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'That email is being used')
                        return redirect_register(**kwargs)
                    else:
                        add_user_login(first_name, last_name, username, email)
                        change_password(email, password)

            # Add new student
            add_student(course, first_name, last_name, username, email)
            messages.success(request, 'You are now registered and can log in')
            return redirect_login(**kwargs)
        else:
            messages.error(request, 'Passwords do not match')
            return redirect_register(**kwargs)
    else:
        data = page_settings(page=f'course/{course}', course=course)
        return render(request, 'register.html', data)


def student_login(request, **kwargs):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        u = User.objects.get(email=email)
        user = auth.authenticate(username=u.username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect(f'/course/{kwargs.get("course")}')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect(f'/course/{kwargs.get("course")}/login')
    else:
        course = kwargs.get("course")
        data = page_settings(page=f'course/{course}', course=course)
        return render(request, 'login.html', data)


def student_logout(request, **kwargs):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect(f'/course/{kwargs.get("course")}')