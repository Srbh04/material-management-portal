from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def facultyRegister(request):
    form=CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'facultyregister.html',{'form':form})

def facultyLogin(request):
    if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request, username=username, password=password)  

            if user is not None:
                login(request,user)
                return render(request,'home.html')

    return render(request,'facultylogin.html')


def facultyLogout(request):
    logout(request)
    return redirect('facultyLogin')