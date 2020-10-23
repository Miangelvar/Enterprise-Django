from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# home, about, services, store, contact, blog

def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")




def store(request):
    return render(request, "core/store.html")



