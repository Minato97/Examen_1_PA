from doctest import ELLIPSIS_MARKER
from email.mime import application
from tkinter import N
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
        self.ui.btn_Registrar.setEnabled(False)
        self.ui.btn_Registrar.setToolTip("Analizar la información")
        int_validator = QIntValidator()
        self.ui.claveCarrera.setValidator(int_validator)
        self.ui.nombreCarrera.textChanged.connect(self.habilitarBtnRegistrar)
        self.ui.claveCarrera.textChanged.connect(self.habilitarBtnRegistrar)
        # self.ui.btn_registrar.clicked.connect(self.registrarCarrera)
        
    def habilitarBtnRegistrar(self):
        if len(self.ui.nombreCarrera.text())>0 and len(self.ui.claveCarrera.text())>0:
            self.ui.btn_Registrar.setEnabled(True)
        else:
            self.ui.btn_Registrar.setEnabled(False)
            # self.ui.lblResultado.setText("")

aplicacion = QtWidgets.QApplication([])
mi_sistema = Sistema()
mi_sistema.show()

sys.exit(aplicacion.exec_())