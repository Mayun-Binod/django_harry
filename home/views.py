from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        "variable1":"binod",
        "variable2":"saroj",
    }
    # return HttpResponse('this is home/index page')
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse('this is about page')
    return render(request,'about.html') 

def services(request):
    # return HttpResponse('this is services page')
    return render(request,'services.html') 

def contact(request):
    # return HttpResponse('this is contact page')
    return render(request,'contact.html')