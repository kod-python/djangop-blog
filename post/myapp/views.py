from django.shortcuts import render
from django.http import HttpResponse
from .models import Features
from .models import Infos

# Create your views here.


def index(request):
     
    features = Features.objects.all()
     
  
      
    
    return render(request, 'index.html', {'features':features})




def trial(request):
    
    formations = Infos()
    
    formations.id = 0
    formations.name = 'joe'
    formations.age = '23'
    formations.desc = 'he is a nice person'
    formations.wealth = '$ 1million'
    bool = True
    
    
    formations1 = Infos()
    
    formations1.id = 1
    formations1.name = 'peter'
    formations1.age = '25'
    formations1.desc = 'he is a good person'
    formations1.wealth = '$ 2million'
    
    
    
    formations2 = Infos()
    
    formations2.id = 2
    formations2.name = 'john'
    formations2.age = '29'
    formations2.desc = 'he is brillian'
    formations2.wealth = '$ 3million'
    
    
    formations = [formations,formations1,formations2]
    
    return render(request, 'trial.html', {'formations':formations})
