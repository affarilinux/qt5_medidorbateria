from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QCheckBox,QSpinBox
from PyQt5 import QtCore

'''
    CONFIGURACOES APP
'''
from configuracoesapp.numero import (
    NUM5,NUM10,NUM20,NUM40,NUM140,NUM180,NUM200
    )
from configuracoesapp.letra import false_lt

class GUIFront2(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        # frame janela

        LABEL2_JANERLA = QLabel(self)
        LABEL2_JANERLA.move(NUM5,NUM10)
        LABEL2_JANERLA.resize(190,380)
        LABEL2_JANERLA.setStyleSheet('QLabel{background-color: #FFFF00;}')# YELLOW

        self.botao2_janela= QPushButton('BATERIA',self)
        self.botao2_janela.move(NUM10,NUM20)#janela
        self.botao2_janela.resize(NUM180,NUM40)
        self.botao2_janela.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_janela.clicked.connect(self.whidget_bateria)

        self.botao2_janela2= QPushButton('RAM',self)
        self.botao2_janela2.move(NUM10,80)#janela
        self.botao2_janela2.resize(NUM180,NUM40)
        self.botao2_janela2.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_janela2.clicked.connect(self.whidget_ram)

        self.botao2_janela3= QPushButton('TEMPERATURA',self)
        self.botao2_janela3.move(NUM10,NUM140)#janela
        self.botao2_janela3.resize(NUM180,NUM40)
        self.botao2_janela3.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_janela3.clicked.connect(self.whidget_temperatura)

        self.botao2_janela4= QPushButton('COOLER',self)
        self.botao2_janela4.move(NUM10,NUM200)#janela
        self.botao2_janela4.resize(NUM180,NUM40)
        self.botao2_janela4.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_janela4.clicked.connect(self.Whidget_cooler)

        self.botao2_janela5= QPushButton('PROCESSADOR',self)
        self.botao2_janela5.move(NUM10,260)#janela
        self.botao2_janela5.resize(NUM180,NUM40)
        self.botao2_janela5.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_janela5.clicked.connect(self.widget_processador)

        self.botao2_conf= QPushButton('CONFIGURAÇÕES',self)
        self.botao2_conf.move(NUM10,320)#janela
        self.botao2_conf.resize(NUM180,NUM40)
        self.botao2_conf.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_conf.clicked.connect(self.whidget_configuracoes)

    def Whidget_cooler1(self):

        self.LABEL_4x_COO = QLabel(self)
        self.LABEL_4x_COO.move(NUM200,160)
        self.LABEL_4x_COO.resize(590,60)
        self.LABEL_4x_COO.setStyleSheet('QLabel{background-color: #FF00FF;font: bold; font-size: 50px}')# 
        self.LABEL_4x_COO.setAlignment(QtCore.Qt.AlignCenter)
        self.LABEL_4x_COO.show()


    def widget_processador1(self):

        self.botao_grap_p= QPushButton('GRAFICO',self)
        self.botao_grap_p.move(350,50)#janela
        self.botao_grap_p.resize(200,NUM40)
        self.botao_grap_p.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 20px}')#RED
        self.botao_grap_p.show()
        self.botao_grap_p.clicked.connect(self.botao_grafico_processador)

        self.LABEL_AP = QLabel(self)
        self.LABEL_AP.move(220,125)
        self.LABEL_AP.setText("  * BOTÂO ATIVA E DESATIVA.")
        self.LABEL_AP.resize(220,20)
        self.LABEL_AP.setStyleSheet('QLabel{background-color: #00FF00; font: italic;font-size: 14px}')# 
        self.LABEL_AP.show()

        self.LABEL_LIN = QLabel(self)
        self.LABEL_LIN.move(NUM200,150)
        self.LABEL_LIN.resize(590,7)
        self.LABEL_LIN.setStyleSheet('QLabel{background-color: #228B22}')# 
        self.LABEL_LIN.show()

        self.QCB_C = QCheckBox("ATIVAR CONTROLE",self)
        self.QCB_C.setChecked( false_lt )
        self.QCB_C.move(220,170)
        self.QCB_C.resize(290,30)
        self.QCB_C.setStyleSheet('QCheckBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.QCB_C.stateChanged.connect(self.widget_processador12) 
        self.QCB_C.show()

        self.spin = QSpinBox(self)
        self.spin.move(220,210)
        self.spin.resize(100,30)
        self.spin.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.spin.setMaximum(100)
        self.spin.setMinimum(1)
        self.spin.valueChanged.connect(self.widget_processador121)
        self.spin.show()

        self.spin_jan2_frameproc()

        self.LABEL_INFO = QLabel(self)
        self.LABEL_INFO.move(220,290)
        self.LABEL_INFO.setText("  * SOMENTE ATIVADO PODERÁ SALVAR AS INFORMAÇÕES.")
        self.LABEL_INFO.resize(420,20)
        self.LABEL_INFO.setStyleSheet('QLabel{background-color: #00FF00; font: italic;font-size: 14px}')# 
        self.LABEL_INFO.show()

        self.LABEL_INFO_NUM = QLabel(self)
        self.LABEL_INFO_NUM.move(220,315)
        self.LABEL_INFO_NUM.setText("  * VALIDO ENTRE 1 A 100%.")
        self.LABEL_INFO_NUM.resize(420,20)
        self.LABEL_INFO_NUM.setStyleSheet('QLabel{background-color: #00FF00; font: italic;font-size: 14px}')# 
        self.LABEL_INFO_NUM.show()

    def print_salvo_processador(self):

        self.LABEL_PRINT = QLabel(self)
        self.LABEL_PRINT.move(380,210)
        self.LABEL_PRINT.setText("SALVO")
        self.LABEL_PRINT.resize(130,30)
        self.LABEL_PRINT.setStyleSheet('QLabel{background-color: #1E90FF; font: italic;font-size: 25px}')# DodgerBlue
        self.LABEL_PRINT.setAlignment(QtCore.Qt.AlignCenter)
        self.LABEL_PRINT.show()

    def whidget_configuracoes_6(self):

        
        self.botao_resert= QPushButton('RESERT',self)
        self.botao_resert.move(220,NUM20)#janela
        self.botao_resert.resize(NUM180,NUM40)
        self.botao_resert.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao_resert.clicked.connect(self.apagar_registro)
        self.botao_resert.show()

        self.LABEL_INF_RESERT = QLabel(self)
        self.LABEL_INF_RESERT.move(220,70)
        self.LABEL_INF_RESERT.setText("  * INICIA TODAS AS INFORMAÇÕES.")
        self.LABEL_INF_RESERT.resize(300,20)
        self.LABEL_INF_RESERT.setStyleSheet('QLabel{background-color: #00FF00; font: italic;font-size: 14px}')# 
        self.LABEL_INF_RESERT.show()
    






    


        

    
        

       
        
        
        
        