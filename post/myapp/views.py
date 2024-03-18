from django.shortcuts import render
from django.http import HttpResponse
from .models import Features

# Create your views here.


def index(request):
     
    features = Features.objects.all()
     
  
      
    
    return render(request, 'index.html', {'features':features})




def trial(request):
    return render(request, 'trial.html')
