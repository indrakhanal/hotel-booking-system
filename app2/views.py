from django.shortcuts import render, redirect, HttpResponse
from.models import AddRoom, FillCostumerForm, CheckAvailable
from.forms import CostumerForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def add_room(request):
    room_data = AddRoom.objects.all()
    context = {
        'room_data': room_data
    }
    return render(request, 'app1/homepage.html', context)


def costumer_fill_form(request):
    try:
        if request.method == 'GET':
            context = {
                'form': CostumerForm()
            }
            return render(request, 'app1/fill_form.html', context)
        else:
            form = CostumerForm(request.POST or request.FILES)
            if form.is_valid():
                form.save()
            messages.add_message(request, messages.SUCCESS, 'your room is successfully booked THANKS FOR CHOOSING US')
            return redirect('home')

    except:
        messages.add_message(request, messages.ERROR, 'Something Went Wrong')
        return redirect('fill_form')


@login_required(login_url='sign_up')
def check_room_available(request):
    if request.method == 'GET':
        return render(request, 'app1/check_available.html')
    else:
        room_no = request.POST.get('room_no')
        if room_no != '':
            try:
                check = FillCostumerForm.objects.get(room_num=room_no)
                room_number = check.room_num
                if room_no == room_number:
                    messages.add_message(request, messages.SUCCESS, 'Sorry this room is already have booked')
                    return redirect('check')

            except:
                # check_in = request.POST.get('check_in')
                # check_out = request.POST.get('check_out')
                # update = CheckAvailable(check_in_date=check_in, check_out_date=check_out, room_no=room_no)
                # update.save()
                messages.add_message(request, messages.ERROR, 'This room is available you can book now')
                return redirect('fill_form')

        else:
            messages.add_message(request, messages.SUCCESS, 'please enter room number')
            return redirect('check')


def search_room(request):
    room = request.POST.get('select')
    context = {
        'room': room
    }
    return render(request, 'app1/check_available.html', context)


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'login/signin.html')
    else:
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            context = {
                'user': user
            }
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'username or password not correct')
            return redirect('sign_in')


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'login/signup.html')
    else:
        u = request.POST.get("username")
        p1 = request.POST.get("password1")
        p2 = request.POST.get("password2")
        if p1 == p2:
            try:
                user = User(username=u)
                user.set_password(p2)
                user.save()
                messages.add_message(request, messages.SUCCESS, 'YOUR ACCOUNT HAS SUCCESSFULLY CREATED')
                return redirect('home')
            except:
                messages.add_message(request, messages.ERROR, 'This username already exist please choose another')
                return redirect('sign_up')
        else:
            messages.add_message(request, messages.ERROR, 'password does not match')


def logout_(request):
    logout(request)
    return redirect('home')


@login_required(login_url='sign_in')
def activity(request):
    return render(request, 'login/Activity.html')


@login_required(login_url='sign_in')
def user_activity(request):
    c_data = FillCostumerForm.objects.get(id=request.user.id)
    context = {
        'c_data': c_data
    }
    return render(request, 'login/Activity.html', context)

