from django.shortcuts import render, get_object_or_404


# Create your views here.
from pages.models import Page


def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html', {'page': page})