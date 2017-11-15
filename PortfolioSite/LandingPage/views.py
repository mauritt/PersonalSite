from django.shortcuts import render, get_object_or_404
from .models import Details

def index(request):
    details = get_object_or_404(Details, id=1)
    context = {'details': details}
    return render(request, "LandingPage/index.html", context)
