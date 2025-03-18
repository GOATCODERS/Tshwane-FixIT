from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def main(request):
    return HttpResponse("hello")