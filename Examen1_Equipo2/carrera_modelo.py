
carreras = list()
class Carrera:
    
    def __init__(self,clave,nombre):
        self.__nombre = nombre
        self.__alumnos = list()
        self.__ClaveCarrera = clave

    def getCarrera(self):
        return self.__nombre

    def getClaveCarrera(self):
        return self.__ClaveCarrera

    def getAlumnosC(self):
        return self.__alumnos
    
    def setClaveCarrera(self, clave):
        self.__ClaveCarrera = clave

    def setAlumnosC(self,alumno):
        self.__alumnos.append(alumno)

    def setNombre(self,nombre):
        self.__nombre = nombre

    def listarAlumnosC(self, carrera):
        print("""      Los alumnos registradas a la carrera son: """)
        for alum in carrera.__alumnos:
            print(alum.getMatricula(),"\t",alum.getAlumno(),"\t",alum.getFechanacimiento(),"\t",alum.getFechaingreso(),"\t",alum.getGenero(),"\t",alum.getCiudad())

