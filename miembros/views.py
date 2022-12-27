from django.shortcuts import render
from django.http import HttpResponse

from miembros.models import Members

def addMember(request):
    new_member = Members.objects.create(familiarType = 'Hermano', name='Sebastian Pedersen', age=16, occupation='Estudiante', isEmployed = False)
    return HttpResponse('Nuevo miembro añadido')

def listadoMiembros(request):
    all_members = Members.objects.all()
    context = {
        'members':all_members,
    }
    return render(request, 'listadoMiembros.html', context=context)