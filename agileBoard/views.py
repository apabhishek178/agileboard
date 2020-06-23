from django.shortcuts import redirect
from django.http import HttpResponse
def homepage(request):
    return HttpResponse("<h1>welcome to the agile-inhouse board </h1>")
