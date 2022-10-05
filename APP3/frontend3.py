from PyQt5.QtWidgets import QMainWindow,QLabel
from PyQt5 import QtCore
'''
    CONFIGURACOES APP
''' 
from configuracoesapp.string_letra import RAM_S,PROCESSADOR
class FrontEnd3(QMainWindow):

    def __init__( self ):
            
        super ().__init__() # metodo construtor

        
        self.LABEL3_AVISO = QLabel(self)
        self.LABEL3_AVISO.move(5,10)
        self.LABEL3_AVISO.setText("** AVISO **")
        self.LABEL3_AVISO.resize(240,40)
        self.LABEL3_AVISO.setStyleSheet('QLabel{background-color: #00FF00; font: bold;font-size: 35px}')# 
        self.LABEL3_AVISO.setAlignment(QtCore.Qt.AlignCenter)
       
        self.LABEL3_BAT = QLabel(self)
        self.LABEL3_BAT.move(35,70)
        self.LABEL3_BAT.setText("BATERIA")
        self.LABEL3_BAT.resize(180,25)
        self.LABEL3_BAT.setStyleSheet('QLabel{background-color: #FF4500; font: bold;font-size: 20px}')# 
        self.LABEL3_BAT.setAlignment(QtCore.Qt.AlignCenter)

        self.LABEL3_RAM = QLabel(self)
        self.LABEL3_RAM.move(35,100)
        self.LABEL3_RAM.setText(RAM_S)
        self.LABEL3_RAM.resize(180,25)
        self.LABEL3_RAM.setStyleSheet('QLabel{background-color: #FF4500; font: bold;font-size: 20px}')# 
        self.LABEL3_RAM.setAlignment(QtCore.Qt.AlignCenter)

        self.LABEL3_TEMP = QLabel(self)
        self.LABEL3_TEMP.move(35,130)
        self.LABEL3_TEMP.setText("TEMPERATURA")
        self.LABEL3_TEMP.resize(180,25)
        self.LABEL3_TEMP.setStyleSheet('QLabel{background-color: #FF4500; font: bold;font-size: 20px}')# 
        self.LABEL3_TEMP.setAlignment(QtCore.Qt.AlignCenter)

        self.LABEL3_COOLER = QLabel(self)
        self.LABEL3_COOLER.move(35,160)
        self.LABEL3_COOLER.setText("COOLER")
        self.LABEL3_COOLER.resize(180,25)
        self.LABEL3_COOLER.setStyleSheet('QLabel{background-color: #FF4500; font: bold;font-size: 20px}')# 
        self.LABEL3_COOLER.setAlignment(QtCore.Qt.AlignCenter)

        self.LABEL3_PROC = QLabel(self)
        self.LABEL3_PROC.move(35,190)
        self.LABEL3_PROC.setText(PROCESSADOR)
        self.LABEL3_PROC.resize(180,25)
        self.LABEL3_PROC.setStyleSheet('QLabel{background-color: #FF4500; font: bold;font-size: 20px}')# 
        self.LABEL3_PROC.setAlignment(QtCore.Qt.AlignCenter)

        QtCore.QTimer.singleShot(2000, self.verificar_text_atlabelcor)
        
       
