from django.shortcuts import render
from .models import Curso, Alumno, Profesor
from django.http import HttpResponse

def lista_cursos(req):
    
    lista= Curso.objects.all

    return render(req, "lista_cursos.html",{"lista_cursos": lista})

def inicio(req):

    return render(req, 'inicio.html',{})

def lista_alumnos(req):
    
    lista= Alumno.objects.all

    return render(req, "lista_alumnos.html",{"lista_alumnos": lista})

def lista_profesores(req):
    
    lista= Profesor.objects.all

    return render(req, "lista_profesores.html",{"lista_profesores": lista})



# Create your views here.
