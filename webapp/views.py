from django.shortcuts import render, redirect
from .  forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import *
from django.contrib import messages





def home(request):
    
    return render(request, 'webapp/home.html')

#register

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    context = {'form':form}
    return render(request, 'webapp/register.html', context)

#login
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form':form}
    return render(request, 'webapp/login.html', context)


@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    context = {'records':records}
    return render(request, 'webapp/dashboard.html', context)

@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created successfully')
            return redirect('dashboard')
    context = {'form':form}
    return render(request, 'webapp/create_record.html', context)

@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = CreateRecordForm(instance=record)
    if request.method == 'POST':
        form = CreateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully')
            return redirect('dashboard')
    context = {'form':form}
    return render(request, 'webapp/update_record.html', context)

# read /view singuler record
@login_required(login_url='login')
def view_record(request, pk):
    record = Record.objects.get(id=pk)
    context = {'record':record}
    return render(request, 'webapp/view_record.html', context)

@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, 'Record deleted successfully')
    return redirect('dashboard')

def user_logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('login')
