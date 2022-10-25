
from carrera_modelo import *
from alumno_modelo import *
from datetime import date

import os

def registrarCarreras():
    while True:
        try:
            nombre_carrera = (input("Introduce el nombre de la carrera:"))
            break
        except ValueError:
            print ("Ingrese> ")
    if len(carreras) != 0:
        flag = False
        for carr in carreras:
            if carr.getCarrera() == nombre_carrera:
                print("El nombre {} ya existe, introduce uno distinto".format(nombre_carrera))
                os.system("pause")
                os.system("cls")
                flag = True
                pass
        if flag == False:
            carrera = Carrera(nombre_carrera)
            carreras.append(carrera)
            os.system("cls")
            print("Carrera registrada correctamente")
            os.system("pause")
            os.system("cls")
            pass
    else:
        carrera = Carrera(nombre_carrera)
        carreras.append(carrera)
        os.system("cls")
        print("Carrera registrada correctamente")
        os.system("pause")
        os.system("cls")
        pass

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