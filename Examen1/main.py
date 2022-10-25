
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
        self.ui.btn_registrar.clicked.connect(self.prueba)
        
    def habilitarBtnRegistrar(self):
        if len(self.ui.nombreCarrera.text())>0 and len(self.ui.claveCarrera.text())>0:
            self.ui.btn_registrar.setEnabled(True)
        else:
            self.ui.btn_registrar.setEnabled(False)
            # self.ui.lblResultado.setText("")

    def prueba(self):
        clave = self.ui.claveCarrera.text()
        nombre = self.ui.nombreCarrera.text()
        self.ui.mensaje.setText(registrarCarreras(clave,nombre))
        
    # def showUsers():
    #     registredUsers = DB.database.select_all_users()
    #     loginAdmin.userTable.clear()
    #     row = 0
    #     for user in registredUsers:
    #             column = 0
    #             loginAdmin.userTable.insertRow(row)
    #             for element in user:
    #                     cell = QtWidgets.QTableWidgetItem(element)
    #                     loginAdmin.userTable.setItem(row, column, cell)
    #                     column +=1
    #             row +=1

aplicacion = QtWidgets.QApplication([])
mi_sistema = Sistema()
mi_sistema.show()

sys.exit(aplicacion.exec_())