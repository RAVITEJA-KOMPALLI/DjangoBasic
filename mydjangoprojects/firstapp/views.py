from django.shortcuts import render
from django.http import HttpResponse

def hi(request):
    return render(request, 'firstapp/hello.html');
    #return HttpResponse('<h1>This is our first django framework</h1>')

# Create your views here.
