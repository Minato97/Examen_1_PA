
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
        int_validator = QIntValidator()
        #Boton para registrar carrera
        self.ui.btn_registrar.setEnabled(False)
        self.ui.btn_registrar.setToolTip("Registrar Carrera")
        self.ui.claveCarrera.setValidator(int_validator)
        self.ui.nombreCarrera.textChanged.connect(self.habilitarBtnRegistrar)
        self.ui.claveCarrera.textChanged.connect(self.habilitarBtnRegistrar)
        self.ui.btn_registrar.clicked.connect(self.btnRegistrar)

        #Boton para registrar alumno
        self.ui.A_btnRegistrar.setEnabled(False)
        self.ui.A_btnRegistrar.setToolTip("Registrar Alumno")
        self.ui.A_noControl.setValidator(int_validator)
        self.ui.A_noControl.textChanged.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_nombreAlumno.textChanged.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_carrera.textActivated.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_genero.textActivated.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_btnRegistrar.clicked.connect(self.A_btnRegistrar)

        #Boton para buscar alumno por matricula
        self.ui.C_btnBuscar_Control.setEnabled(False)
        self.ui.C_btnBuscar_Control.setToolTip("Buscar Alumno")
        self.ui.C_numero_Control.textChanged.connect(self.habilitarBtn_BuscarControl)
        self.ui.C_btnBuscar_Control.clicked.connect(self.C_btnBuscar_Control)

        #Boton para buscar alumnos por carrera
        self.ui.C_btnBuscar_Carrera.setEnabled(False)
        self.ui.C_btnBuscar_Carrera.setToolTip("Buscar Alumno")
        self.ui.C_carrera_Carrera.textActivated.connect(self.habilitarBtn_BuscarCarrera)
        self.ui.C_btnBuscar_Carrera.clicked.connect(self.C_btnBuscar_Carrera)


    #Llenar combo box
    def AddItem_Carrera(self,nombre_carrera):
        for carrera in carreras:
            if carrera.getCarrera() == nombre_carrera:
                self.ui.A_carrera.addItem(carrera.getCarrera())
                self.ui.C_carrera_Carrera.addItem(carrera.getCarrera())


    #Funciones para boton registrar carrera
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


    #Boton para registrar alumno
    def habilitarBtn_ARegistrar(self):
        if len(self.ui.A_noControl.text()) > 0 and len(self.ui.A_nombreAlumno.text()) > 0 and self.ui.A_genero.currentIndex() > 0 and self.ui.A_carrera.currentIndex() > 0:
            self.ui.A_btnRegistrar.setEnabled(True)
        else:
            self.ui.A_btnRegistrar.setEnabled(False)

    def A_btnRegistrar(self):
        clave = self.ui.A_noControl.text()
        nombre = self.ui.A_nombreAlumno.text()
        genero = self.ui.A_genero.currentText()
        nombre_carrera = self.ui.A_carrera.currentText()
        for carrera in carreras:
            if carrera.getCarrera() == nombre_carrera:
                carrerax = carrera

        QtWidgets.QMessageBox.information(self, "Alumno", f"{registrarAlumnosCarrera(clave,nombre,genero,carrerax)}",buttons=QtWidgets.QMessageBox.Ok)
        self.mostrarAlumnos()
        self.ui.A_noControl.clear()
        self.ui.A_nombreAlumno.clear()
        self.ui.A_genero.setCurrentIndex(0)
        self.ui.A_carrera.setCurrentIndex(0)

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


    #Funciones de boton para buscar alumno por clave
    def habilitarBtn_BuscarControl(self):
        if len(self.ui.C_numero_Control.text()) > 0:
            self.ui.C_btnBuscar_Control.setEnabled(True)
        else:
            self.ui.C_btnBuscar_Control.setEnabled(False)

    def C_btnBuscar_Control(self):
        clave = self.ui.C_numero_Control.text()
        self.ui.C_tabla_Control.clearContents()
        self.ui.C_tabla_Control.removeRow(0)
        retorno, flag, carrera = buscarAlumno(clave)
        if flag == True:
            self.mostrarAlumnoEncontrado(retorno, carrera)
        else:
            QtWidgets.QMessageBox.warning(self, "Alumno",f"El alumno con el número de control {retorno} no existe.", buttons=QtWidgets.QMessageBox.Ok)
        self.ui.C_numero_Control.clear()


    def mostrarAlumnoEncontrado(self,alumno, carrera):
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


    #Funciones para buscar alumnos por carrera
    def habilitarBtn_BuscarCarrera(self):
        if self.ui.C_carrera_Carrera.currentIndex() > 0:
            self.ui.C_btnBuscar_Carrera.setEnabled(True)
        else:
            self.ui.C_btnBuscar_Carrera.setEnabled(False)

    def C_btnBuscar_Carrera(self):
        self.ui.C_tabla_Carrera.clearContents()
        self.ui.C_tabla_Carrera.removeRow(0)
        nombreCarrera = self.ui.C_carrera_Carrera.currentText()
        for carrera in carreras:
            if carrera.getCarrera() == nombreCarrera:
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
        self.ui.C_carrera_Carrera.setCurrentIndex(0)


aplicacion = QtWidgets.QApplication([])
mi_sistema = Sistema()
mi_sistema.show()

sys.exit(aplicacion.exec_())