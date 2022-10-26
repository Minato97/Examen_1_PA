
from carrera_modelo import *
from alumno_modelo import *

import os

def registrarCarreras(clave,nombre):      
    if len(carreras) != 0:
        flag = False
        for carr in carreras:
            if carr.getClaveCarrera() == clave:
                return "La clave {} ya existe, introduce una distinta".format(clave)
        if flag == False:
            carrera = Carrera(clave,nombre)
            carreras.append(carrera)
            return "Carrera registrada correctamente"
    else:
        carrera = Carrera(clave,nombre)
        carreras.append(carrera)
        return "Carrera registrada correctamente"


def listarCarreras():
    if len(carreras) >=1:
       # print("No se tienen carreras registradas")
    # else:
    #     os.system("cls")
        # print("""      Las carreras existentes son: """)
        for carr in carreras:
            print(carr.getCarrera())

def registrarAlumnosCarrera(clave, nombre, genero):
    carr = Carrera()
    if len(Carrera.getAlumnosC(alumnos)) != 0:
        flag = False
        alumno = Carrera()
        for alum in alumno.getMatricula():
            if alum.getMatricula() == clave:
                return f"La clave {clave} ya existe, introduce una distinta"
        if flag == False:
            alumno=Alumno(clave)
            alum.setAlumnosC(clave, nombre, genero)
            return "Alumno registrado correctamente"
        else:
            alumno = Alumno(clave, nombre, genero)
            alum.setAlumnosC(alumno)

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