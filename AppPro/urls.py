
from django.urls import path
from AppPro.views import lista_cursos, inicio, lista_alumnos, lista_profesores

urlpatterns = [
    path('lista_cursos/', lista_cursos, name='cursos'),
    path('lista_alumnos/', lista_alumnos, name='alumnos'),
    path('lista_profesores/', lista_profesores, name= 'profesores'),
    path('', inicio, name='inicio'),
]
