

class Alumno:

    def __init__(self):
        self.__matricula = int
        self.__nombre = str
        self.__genero = str

    def getMatricula(self):
        return self.__matricula

    def getAlumno(self):
        return self.__nombre

    def getGenero(self):
        return self.__genero

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setGenero(self, genero):
        self.__genero = genero
