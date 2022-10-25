
from carrera_modelo import *
from alumno_modelo import *

import os

def registrarCarreras(clave,nombre):      
    if len(carreras) != 0:
        flag = False
        for carr in carreras:
            if carr.getClaveCarrera() == clave:
                return "La clave {} ya existe, introduce una distinto".format(clave)
        if flag == False:
            carrera = Carrera(clave,nombre)
            carreras.append(carrera)
            return "Carrera registrada correctamente"
    else:
        carrera = Carrera(clave,nombre)
        carreras.append(carrera)
        return "Carrera registrada correctamente"

def listarCarreras():
    if len(carreras) == 0:
        os.system("cls")
        print("No se tienen carreras registradas")
        os.system("pause")
        os.system("cls")
        pass
    else:
        os.system("cls")
        print("""      Las carreras existentes son: """)
        for carr in carreras:
            print(carr.getCarrera())
        os.system("pause")
        os.system("cls")
        pass

def registrarAlumnosCarrera():
    nombre_carrera = input("Introduce el nombre de la carrera: ")
    for carr in carreras:
        if carr.getCarrera() == nombre_carrera:
            print("Ingresa los siguientes datos del alumno: ")
            alumno = Alumno()
            alumno.setMatricula((input("Matricula: ")))
            alumno.setNombre(input("Nombre: "))
            alumno.setGenero(input("Genero (M/F): "))
            carr.setAlumnosC(alumno)
            print("\n-----Alumno registrado exitosamente-----")
            os.system("pause")
            os.system("cls")
            pass
        else:
            os.system("cls")
            print("La carrera no fue encontada, no es posible registrar alumnos.")
            pass

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