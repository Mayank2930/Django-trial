from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    my_context = {
        "my_text" : "Loren Epsum blah lalala",
        "my_id" : "1234567"
    } 
    return render(request, "home.html", my_context)

