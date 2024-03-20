from django.shortcuts import render
from django.http import HttpResponse
from cats.models import Student
from cats.models import Cat

def index(request):
    student_list = Student.objects.order_by('last_name')
    cats_list = Cat.objects.order_by('name')

    context_dict = {}
    context_dict['students'] =  student_list
    context_dict['cats'] = cats_list
    return render(request, 'cats/index.html', context=context_dict)

def about(request):
    cats_list = Cat.objects.order_by('name')

    context_dict = {}
    context_dict['cats'] = cats_list
    return render(request, 'cats/about.html', context=context_dict)

# Create your views here.
