from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"index.html")

def success_page(request):
    print('*'*10)
    return HttpResponse("<h2> hey this is a success page</h2>")

def new(request):
    peoples=[
        {"name": "Vidhi", "age":17},
        {"name": "naved", "age":28},
        {"name": "hasan", "age":27}
    ]

    text="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt numquam voluptate ipsa commodi recusandae vel, et laboriosam doloribus sint aperiam magni omnis aliquid aliquam dolor? Rem voluptate laboriosam omnis cupiditate!"""

    return render(request,"index.html",context={'peoples':peoples})

def about(request):
    return render(request,'about.html')

def contact(request):
    context={'page':'Contact'}
    return render(request,'contact.html',context)
# Create your views here.
