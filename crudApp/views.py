from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentForm
from.models import Student
from django.contrib import messages
from django.db.models import Q

# This Function Will Add  Show Students Data And Also Search Records
def home(request):
    query = request.GET.get('searchquery')

    if query:
        students = Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(password__icontains=query))
        messages.success(request, 'Records Found SuccessFully')
    else:
        students = Student.objects.all()
        
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data.get('name')
            em = form.cleaned_data.get('email')
            pw = form.cleaned_data.get('password')
            finnal = Student(name=nm, email=em, password=pw)
            finnal.save()
            messages.success(request, 'Records Added SuccessFully')
            form = StudentForm()
    else:
        form = StudentForm()
        
    context = {'form': form, 'students': students, 'query': query}
    return render(request, 'AddandShow.html', context)



#This Function Will Simply Delete Students Data

def delete_data(request, id):
    if request.method == 'POST':
        data = Student.objects.get(pk=id)
        data.delete()
        messages.success(request, 'Records Deleted SuccessFully')
    return HttpResponseRedirect('/')


def update_data(request, id):
    pi = Student.objects.get(pk=id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated Successfully')
            return HttpResponseRedirect('/')
    else:
        form = StudentForm(instance=pi)
        
    return render(request, 'update.html', {'form': form})