from django.shortcuts import render, get_object_or_404
from .models import alumnoT, Frase
# Create your views here.
def Index_vista(request):
    misalumnos=alumnoT.objects.all().order_by("id")
    return render(request,"index.html",{"misalumnos":misalumnos})

def alumno_vista(request,id):
    alumno = get_object_or_404 (alumnoT,id=id)
    return render(request,"alumno.html",{"objeto":alumno})