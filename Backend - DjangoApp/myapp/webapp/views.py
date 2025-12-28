from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    info =[
        {
        "name":"Nguyễn Văn Tường",
        "email": "22130215@gmail.com",
        "age":15
         },
        {
            "name": "Hồ Hoàng Long",
            "email": "22134215@gmail.com",
            "age": 21
        },
        {
            "name": "Lê Vĩnh Hằng",
            "email": "26130215@gmail.com",
            "age": 35
        },
    ]
    return render(request, 'index.html', {"info": info})
def detail(request, id):
    return HttpResponse(id)