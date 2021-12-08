# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
# Models
from simulations.models import Simulation 


@login_required(login_url='/')
def list_simulation_view(request):
    simulations = Simulation.objects.all().order_by('created_at') 
    return render(request,'simulations/list.html',{'simulations':simulations})

@login_required(login_url='/')
def simulation_view(request,id):
    simulation = Simulation.objects.get(id=id)
    url =  {
        'Parabolic':'simulations/parabolico.html',
        'MRU':'simulations/mru.html',
    }
    return render(request,url[simulation.title],{'simulation':simulation})