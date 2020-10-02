from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
# Create your views here.
def indexview(request):
    form=StudentForm()
    if request.method == 'POST':
            form=StudentForm(request.POST)
            if form.is_valid():
                form.save()
                
    context={'form':form}
    return render(request,'index.html',context)
