
from PyQt5 import QtWidgets
from carrera_controlador import *
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
        self.ui.btn_registrar.setEnabled(False)
        self.ui.btn_registrar.setToolTip("Analizar la información")
        int_validator = QIntValidator()
        self.ui.claveCarrera.setValidator(int_validator)
        self.ui.nombreCarrera.textChanged.connect(self.habilitarBtnRegistrar)
        self.ui.claveCarrera.textChanged.connect(self.habilitarBtnRegistrar)
        self.ui.A_noControl.setValidator(int_validator)
        self.ui.A_noControl.textChanged.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_nombreAlumno.textChanged.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_carrera.textActivated.connect(self.habilitarBtn_ARegistrar)
        self.ui.A_genero.textActivated.connect(self.habilitarBtn_ARegistrar)
        self.ui.btn_registrar.clicked.connect(self.btnRegistrar)
        self.ui.A_btnRegistrar.clicked.connect(self.A_btnRegistrar)

    def habilitarBtn_ARegistrar(self):
        if len(self.ui.A_noControl.text())>0 and len(self.ui.A_nombreAlumno.text())>0 and self.ui.A_genero.currentIndex()>0 and self.ui.A_carrera.currentIndex()>0:
            self.ui.A_btnRegistrar.setEnabled(True)
        else: 
            self.ui.A_btnRegistrar.setEnabled(False)
    
    def AddItem_Carrera(self):
        for carrera in carreras:
            self.ui.A_carrera.addItem(carrera.getCarrera())
        
    def habilitarBtnRegistrar(self):
        if len(self.ui.nombreCarrera.text())>0 and len(self.ui.claveCarrera.text()) > 0:
            self.ui.btn_registrar.setEnabled(True)
        else:
            self.ui.btn_registrar.setEnabled(False)
            # self.ui.lblResultado.setText("")

    def btnRegistrar(self):
        clave = self.ui.claveCarrera.text()
        nombre = self.ui.nombreCarrera.text()
        self.ui.mensaje.setText(registrarCarreras(clave,nombre))
        self.mostrarCarreras()
        
    def A_btnRegistrar(self):
        pass
        
        
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