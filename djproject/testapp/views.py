from django.shortcuts import render
from testapp.models import *

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)

def blorejobs(request):
    return render(request,'testapp/blorejobs.html')

def punejobs(request):
    return render(request,'testapp/punejobs.html')

def chennaijobs(request):
    return render(request,'testapp/chennaijobs.html')
