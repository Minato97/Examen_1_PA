
carreras = list()
class Carrera:
    # __nombre = None
    # __materias = None

    def __init__(self,carrera):
        self.__nombre = carrera
        self.__alumnos = list()
        self.__ClaveCarrera = list()

    def getCarrera(self):
        return self.__nombre


    def getAlumnosC(self):
        return self.__alumnos

    def setAlumnosC(self,alumno):
        self.__alumnos.append(alumno)

    def setNombre(self,nombre):
        self.__nombre = nombre

    # def addMateria(self,materia):
    #     self.__materias.append(materia)

    def listarAlumnosC(self, carrera):
        print("""      Los alumnos registradas a la carrera son: """)
        for alum in carrera.__alumnos:
            print(alum.getMatricula(),"\t",alum.getAlumno(),"\t",alum.getFechanacimiento(),"\t",alum.getFechaingreso(),"\t",alum.getGenero(),"\t",alum.getCiudad())

