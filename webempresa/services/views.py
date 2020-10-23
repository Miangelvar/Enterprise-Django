from django.shortcuts import render

# Create your views here.
from services.models import Service


def services(request):
    services = Service.objects.all()
    return render(request, "services/services.html", {"services": services})
