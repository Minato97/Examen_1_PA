from carrera_modelo import *
from alumno_modelo import *
from carrera_controlador import *

def buscarAlumno(clave):
    for carrera in carreras:
        for alumno in carrera.getAlumnosC():
            if alumno.getMatricula() == clave:
                return alumno, True, carrera
    return clave, False, None

