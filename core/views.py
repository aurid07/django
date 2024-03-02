from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requests):
    return HttpResponse('<h1>welcome to social book</h1>')