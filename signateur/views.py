from django.shortcuts import render
from .models import Signateur
# Create your views here.
def home(request):
    signateurs = Signateur.objects.all()
    for signateur in signateurs:
        print(signateur.img_data)
    return render(request ,'home.html',{"signateurs":signateurs})