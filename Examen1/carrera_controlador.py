
from carrera_modelo import *
from alumno_modelo import *

import os

def registrarCarreras(clave,nombre):      
    if len(carreras) != 0:
        flag = False
        for carr in carreras:
            if carr.getClaveCarrera() == clave:
                return True, clave
        if flag == False:
            carrera = Carrera(clave,nombre)
            carreras.append(carrera)
            return False, nombre
    else:
        carrera = Carrera(clave,nombre)
        carreras.append(carrera)
        return False, nombre

# def listarCarreras():
#     if len(carreras) >=1:
#        # print("No se tienen carreras registradas")
#     # else:
#     #     os.system("cls")
#         # print("""      Las carreras existentes son: """)
#         for carr in carreras:
#             print(carr.getCarrera())

def registrarAlumnosCarrera(clave,nombre,genero,carrera):
    alumno = Alumno()
    alumno.setMatricula(clave)
    alumno.setNombre(nombre)
    alumno.setGenero(genero)
    carrera.setAlumnosC(alumno)
    return "Alumno registrado correctamente"



def listarAlumnosCarrera():
    os.system("cls")
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            carr.listarAlumnosC(carr)
            os.system("pause")
            os.system("cls")
            pass
        else:
            print("El nombre de la carrera no fue encontrada.")
            os.system("pause")
            os.system("cls")
            pass 