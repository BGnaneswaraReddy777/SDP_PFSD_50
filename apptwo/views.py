from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Problem

def insert(request):
    if request.method == "POST":
        proId = request.POST['proId']
        proName = request.POST['proName']
        proGender = request.POST['proGender']
        proEmail = request.POST['proEmail']
        proDesignation = request.POST['proDesignation']
        data = Problem(proId=proId, proName=proName, proGender=proGender, proEmail=proEmail,
                        proDesignation=proDesignation)
        data.save()

        return redirect('show')
    else:
        return render(request, 'insert.html')
from django.contrib.auth.decorators import login_required

def show(request):
    problems = Problem.objects.all()
    return render(request, 'show.html', {'problems': problems})

# Update Employee

def edit(request,pk):
    problems = Problem.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            problems.proName = request.POST['proName']
            problems.proGender = request.POST['proGender']
            problems.proEmail = request.POST['proEmail']
            problems.proDesignation = request.POST['proDesignation']
            problems.proDesignation = request.POST['proDesignation']
            problems.save()
            return redirect('show')
    context = {
        'problems': problems,
    }

    return render(request,'edit.html',context)

#Delete Employee
from django.shortcuts import get_object_or_404, render, redirect
from .models import Problem
from django.http import HttpResponse

def remove(request, pk):
    try:
        problem = get_object_or_404(Problem, id=pk)
    except Problem.DoesNotExist:
        return HttpResponse("Problem not found", status=404)

    if request.method == 'POST':
        # Correct way to delete the instance
        problem.delete()
        return redirect('show')  # Redirect to show page after deletion

    # If it's a GET request (rendering the confirmation page)
    context = {
        'problem': problem,  # Passing the specific problem instance to the template
    }
    return render(request, 'delete.html', context)
