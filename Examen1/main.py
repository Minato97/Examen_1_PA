
from PyQt5 import QtWidgets
from carrera_controlador import *
from alumno_controlador import *
from interfaz import Ui_MainWindow
import sys
from PyQt5.QtGui import QIntValidator
 

class Sistema(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.inicializarGUI()
        
    def inicializarGUI(self):
        '''
        inicializarGUI inicializa la interfaz gráfica del usuario
        '''
        int_validator = QIntValidator()

        self.ui.btn_registrar.setEnabled(False)
        self.ui.btn_registrar.setToolTip("Registrar Carrera")
        self.ui.claveCarrera.setValidator(int_validator)
        self.ui.nombreCarrera.textChanged.connect(self.habilitarBtnRegistrar)
        self.ui.claveCarrera.textChanged.connect(self.habilitarBtnRegistrar)
        self.ui.btn_registrar.clicked.connect(self.btnRegistrar)

        self.ui.A_btnRegistrar.setEnabled(False)
        self.ui.A_btnRegistrar.setToolTip("Registrar Alumno")
        self.ui.A_noControl.setValidator(int_validator)
        self.ui.A_noControl.textChanged.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_nombreAlumno.textChanged.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_carrera.textActivated.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_genero.textActivated.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_btnRegistrar.clicked.connect(self.A_btnRegistrar)

        self.ui.C_btnBuscar_Control.setEnabled(False)
        self.ui.C_btnBuscar_Control.setToolTip("Buscar Alumno")
        self.ui.C_numero_Control.textChanged.connect(self.habilitarBtn_BuscarControl)
        self.ui.C_btnBuscar_Control.clicked.connect(self.C_btnBuscar_Control)

        self.ui.C_btnBuscar_Carrera.setEnabled(False)
        self.ui.C_btnBuscar_Carrera.setToolTip("Buscar Alumno")
        self.ui.C_carrera_Carrera.textActivated.connect(self.habilitarBtn_BuscarCarrera)
        self.ui.C_btnBuscar_Carrera.clicked.connect(self.C_btnBuscar_Carrera)



    def habilitarBtn_ARegistrar(self):
        if len(self.ui.A_noControl.text()) > 0 and len(self.ui.A_nombreAlumno.text()) > 0 and self.ui.A_genero.currentIndex() > 0 and self.ui.A_carrera.currentIndex() > 0:
            self.ui.A_btnRegistrar.setEnabled(True)
        else: 
            self.ui.A_btnRegistrar.setEnabled(False)

    def habilitarBtn_BuscarCarrera(self):
        if len(self.ui.C_carrera_Carrera.currentIndex()) > 0:
            self.ui.C_btnBuscar_Carrera.setEnabled(True)
        else:
            self.ui.C_btnBuscar_Carrera.setEnabled(False)

    def habilitarBtn_BuscarControl(self):
        if len(self.ui.C_numero_Control.text()) > 0:
            self.ui.C_btnBuscar_Control.setEnabled(True)
        else:
            self.ui.C_btnBuscar_Control.setEnabled(False)
    
    def AddItem_Carrera(self,nombre_carrera):
        for carrera in carreras:
            if carrera.getCarrera() == nombre_carrera:
                self.ui.A_carrera.addItem(carrera.getCarrera())
                self.ui.C_carrera_Carrera.addItem(carrera.getCarrera())
        
    def habilitarBtnRegistrar(self):
        if len(self.ui.nombreCarrera.text())>0 and len(self.ui.claveCarrera.text()) > 0:
            self.ui.btn_registrar.setEnabled(True)
        else:
            self.ui.btn_registrar.setEnabled(False)

    def btnRegistrar(self):
        clave = self.ui.claveCarrera.text()
        nombre = self.ui.nombreCarrera.text()
        flag, retorno = registrarCarreras(clave,nombre)
        if flag == True:
            QtWidgets.QMessageBox.warning(self, "Carrera", f"La carrera {retorno} ya existe favor de colocar una distinta.", buttons=QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Carrera", "La carrera ha sido registrada correctamente", buttons=QtWidgets.QMessageBox.Ok)
            self.AddItem_Carrera(retorno)
            self.mostrarCarreras()
            self.ui.claveCarrera.clear()
            self.ui.nombreCarrera.clear()

    def C_btnBuscar_Control(self):
        clave = self.ui.C_numero_Control.text()
        retorno, flag, carrera = buscarAlumno(clave)
        if flag == True:
            self.mostrarAlumnoEncontrado(retorno, carrera)
        else:
            QtWidgets.QMessageBox.warning(self, "Alumno",f"El alumno con el número de control {retorno} no existe.", buttons=QtWidgets.QMessageBox.Ok)


    def mostrarAlumnoEncontrado(self,alumno, carrera):
        self.ui.C_tabla_Carrera.clearContents()
        row = 0
        column = 0
        self.ui.C_tabla_Control.removeRow(row)
        self.ui.C_tabla_Control.insertRow(row)
        cell = QtWidgets.QTableWidgetItem(alumno.getMatricula())
        self.ui.C_tabla_Control.setItem(row, column, cell)
        column += 1
        cell = QtWidgets.QTableWidgetItem(alumno.getAlumno())
        self.ui.C_tabla_Control.setItem(row, column, cell)
        column += 1
        cell = QtWidgets.QTableWidgetItem(alumno.getGenero())
        self.ui.C_tabla_Control.setItem(row, column, cell)
        column += 1
        cell = QtWidgets.QTableWidgetItem(carrera.getCarrera())
        self.ui.C_tabla_Control.setItem(row, column, cell)
        row += 1

    def A_btnRegistrar(self):
        clave = self.ui.A_noControl.text()
        nombre = self.ui.A_nombreAlumno.text()
        genero = self.ui.A_genero.currentText()
        nombre_carrera = self.ui.A_carrera.currentText()
        for carrera in carreras:
            if carrera.getCarrera() == nombre_carrera:
                carrerax = carrera
        registrarAlumnosCarrera(clave,nombre,genero,carrerax)
        self.mostrarAlumnos()
        self.ui.A_noControl.clear()
        self.ui.A_nombreAlumno.clear()
        self.ui.A_genero.clear()
        self.ui.A_carrera.clear()

    def C_btnBuscar_Carrera(self):
        print(1)
        nombreCarrera = self.ui.C_carrera_Carrera.currentText()
        for carrera in carreras:
            if carrera.getCarrera() == nombreCarrera:
                self.ui.C_tabla_Carrera.clearContents()
                row = 0
                for alumno in carrera.getAlumnosC():
                    column = 0
                    self.ui.C_tabla_Carrera.removeRow(row)
                    self.ui.C_tabla_Carrera.insertRow(row)
                    cell = QtWidgets.QTableWidgetItem(alumno.getMatricula())
                    self.ui.C_tabla_Carrera.setItem(row, column, cell)
                    column += 1
                    cell = QtWidgets.QTableWidgetItem(alumno.getAlumno())
                    self.ui.C_tabla_Carrera.setItem(row, column, cell)
                    column += 1
                    cell = QtWidgets.QTableWidgetItem(alumno.getGenero())
                    self.ui.C_tabla_Carrera.setItem(row, column, cell)
                    column += 1
                    cell = QtWidgets.QTableWidgetItem(carrera.getCarrera())
                    self.ui.C_tabla_Carrera.setItem(row, column, cell)
                    row += 1
                row += 1

    def mostrarAlumnos(self):
        self.ui.A_tabla.clearContents()
        row = 0
        for carrera in carreras:
            for alumno in carrera.getAlumnosC():
                column = 0
                self.ui.A_tabla.removeRow(row)
                self.ui.A_tabla.insertRow(row)
                cell = QtWidgets.QTableWidgetItem(alumno.getMatricula())
                self.ui.A_tabla.setItem(row, column, cell)
                column += 1
                cell = QtWidgets.QTableWidgetItem(alumno.getAlumno())
                self.ui.A_tabla.setItem(row, column, cell)
                column += 1
                cell = QtWidgets.QTableWidgetItem(alumno.getGenero())
                self.ui.A_tabla.setItem(row, column, cell)
                column += 1
                cell = QtWidgets.QTableWidgetItem(carrera.getCarrera())
                self.ui.A_tabla.setItem(row, column, cell)
                row += 1

    def mostrarCarreras(self):
        self.ui.tableWidget.clearContents()
        row = 0
        for carrera in carreras:
            column = 0
            self.ui.tableWidget.removeRow(row)
            self.ui.tableWidget.insertRow(row)
            cell = QtWidgets.QTableWidgetItem(carrera.getClaveCarrera())
            self.ui.tableWidget.setItem(row, column, cell)
            column +=1
            cell = QtWidgets.QTableWidgetItem(carrera.getCarrera())
            self.ui.tableWidget.setItem(row, column, cell)
            row +=1

aplicacion = QtWidgets.QApplication([])
mi_sistema = Sistema()
mi_sistema.show()

sys.exit(aplicacion.exec_())