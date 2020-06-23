from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        #extracting data of the user where the username is same as username entered in the login form
        post = User.objects.filter(username=username)
        if post:
            # this runs when the user is recognised
            request.session['username'] = username
            return redirect("dashboard")
        else:
            #when the user is not recognised
            return render(request, 'core/login.html', {})

    return render(request, 'core/login.html', {})


def dashboard(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            room_name = request.POST['room_name']
            return redirect('room',room_name)
        else:
            #check for the autentication issue by checking if username's value equals to the request.user
            post = request.session['username']
            data = request.user
            return render(request, 'core/profile.html', {'user':data})
    return redirect('login')


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('login')

def room(request, room_name):
    if request.session.has_key('username'):
        return render(request, 'core/chatRoom.html', {'room_name' : room_name})
    return redirect('login')

def board(request):
    if request.session.has_key('username'):
        return render(request, 'core/room.html')
    return redirect('login')
