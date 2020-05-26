from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

# Create your views here.

def inicio(request):
    personas = Persona.objects.all()
    context = { 
        'personas': personas
    }
    return render(request, 'index.html', context)

def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        context = {
            'form': form
        }
    else: 
        form = PersonaForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'crear_persona.html', context)

def editarPersona(request, id):
    persona = Persona.objects.get(id = id)

    if request.method == 'GET':
        form = PersonaForm(instance = persona)
        context = {
            'form': form
        }
    else:
        form = PersonaForm(request.POST, instance = persona)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', context)   

def eliminarPersona(request, id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')