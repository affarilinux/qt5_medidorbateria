from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QCheckBox,QSpinBox
from PyQt5 import QtCore

'''
    CONFIGURACOES APP
'''
from configuracoesapp.numero import (
    NUM5,NUM10,NUM20,NUM40,NUM140,NUM180,NUM200
    )
from configuracoesapp.letra import false_lt
from configuracoesapp.string_letra import RAM_S,PROCESSADOR, TEMPERATURA_S,JANELA2,JANELA3,JANELA5,JANELA1
from configuracoesapp.numerostrig import NUMS1,NUMS2,NUMS3

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

        self.botao2_janela2= QPushButton(RAM_S,self)
        self.botao2_janela2.move(NUM10,80)#janela
        self.botao2_janela2.resize(NUM180,NUM40)
        self.botao2_janela2.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_janela2.clicked.connect(self.whidget_ram)

        self.botao2_janela3= QPushButton(TEMPERATURA_S,self)
        self.botao2_janela3.move(NUM10,NUM140)#janela
        self.botao2_janela3.resize(NUM180,NUM40)
        self.botao2_janela3.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_janela3.clicked.connect(self.whidget_temperatura)

        self.botao2_janela4= QPushButton('COOLER',self)
        self.botao2_janela4.move(NUM10,NUM200)#janela
        self.botao2_janela4.resize(NUM180,NUM40)
        self.botao2_janela4.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_janela4.clicked.connect(self.Whidget_cooler)

        self.botao2_janela5= QPushButton(PROCESSADOR,self)
        self.botao2_janela5.move(NUM10,260)#janela
        self.botao2_janela5.resize(NUM180,NUM40)
        self.botao2_janela5.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_janela5.clicked.connect(self.widget_processador)

        self.botao2_conf= QPushButton('CONFIGURAÇÕES',self)
        self.botao2_conf.move(NUM10,320)#janela
        self.botao2_conf.resize(NUM180,NUM40)
        self.botao2_conf.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao2_conf.clicked.connect(self.whidget_configuracoes)

        self.whidget_bateria()

    ##--------------------------------------------
    ## frame 1
    def Whidget_BATERIA(self):

        self.LABEL_INFO_AVISO_BAT = QLabel(self)
        self.LABEL_INFO_AVISO_BAT.move(220,340)
        self.LABEL_INFO_AVISO_BAT.setText("  * IDEAL ENTRE 20 E 80%.")
        self.LABEL_INFO_AVISO_BAT.resize(420,20)
        self.LABEL_INFO_AVISO_BAT.setStyleSheet('QLabel{background-color: #00FF00; font: italic;font-size: 14px}')# 
        self.LABEL_INFO_AVISO_BAT.show()

        self.LABEL_MIM_SPIN = QLabel(self)
        self.LABEL_MIM_SPIN.move(330,210)
        self.LABEL_MIM_SPIN.setText(" MINIMO")
        self.LABEL_MIM_SPIN.resize(100,25)
        self.LABEL_MIM_SPIN.setStyleSheet('QLabel{ font: italic;font-size: 20px}')# 
        self.LABEL_MIM_SPIN.show()

        self.LABEL_MAX_SPIN = QLabel(self)
        self.LABEL_MAX_SPIN.move(330,250)
        self.LABEL_MAX_SPIN.setText(" MAXIMO")
        self.LABEL_MAX_SPIN.resize(100,25)
        self.LABEL_MAX_SPIN.setStyleSheet('QLabel{ font: italic;font-size: 20px}')# 
        self.LABEL_MAX_SPIN.show()

        self.spin_mim = QSpinBox(self)
        self.spin_mim.move(220,210)
        self.spin_mim.resize(100,30)
        self.spin_mim.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.spin_mim.setMaximum(99)
        self.spin_mim.setMinimum(1)
        self.spin_mim.valueChanged.connect(self.if_qcb_batval)
        self.spin_mim.show()

        self.spin_max = QSpinBox(self)
        self.spin_max.move(220,250)
        self.spin_max.resize(100,30)
        self.spin_max.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.spin_max.setMaximum(100)
        self.spin_max.setMinimum(2)
        self.spin_max.valueChanged.connect(self.if_qcb_batval)
        self.spin_max.show()

        self.QCB_C_mm = QCheckBox("  ATIVAR CONTROLE",self)
        self.QCB_C_mm.move(220,170)
        self.QCB_C_mm.resize(250,30)
        self.QCB_C_mm.setStyleSheet('QCheckBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.QCB_C_mm.stateChanged.connect(self.whidget_bateria_val) 
        self.QCB_C_mm.setChecked( False )
        self.QCB_C_mm.show()


     ## frame 3
    def Whidget_TEMPERATURA(self):

        self.LABEL_INFO_AVISO_IMP = QLabel(self)
        self.LABEL_INFO_AVISO_IMP.move(220,340)
        self.LABEL_INFO_AVISO_IMP.setText("  * IDEIAL ENTRE 30 E 50.")
        self.LABEL_INFO_AVISO_IMP.resize(420,20)
        self.LABEL_INFO_AVISO_IMP.setStyleSheet('QLabel{background-color: #00FF00; font: italic;font-size: 14px}')# 
        self.LABEL_INFO_AVISO_IMP.show()
    ## frame 4
    def Whidget_cooler1(self):

        self.LABEL_4x_COO = QLabel(self)
        self.LABEL_4x_COO.move(NUM200,160)
        self.LABEL_4x_COO.resize(590,60)
        self.LABEL_4x_COO.setStyleSheet('QLabel{background-color: #FF00FF;font: bold; font-size: 50px}')# 
        self.LABEL_4x_COO.setAlignment(QtCore.Qt.AlignCenter)
        self.LABEL_4x_COO.show()

    ## frame5
    def widget_processador1(self):

        self.botao_grap_p= QPushButton('GRAFICO',self)
        self.botao_grap_p.move(350,50)#janela
        self.botao_grap_p.resize(200,NUM40)
        self.botao_grap_p.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 20px}')#RED
        self.botao_grap_p.show()
        self.botao_grap_p.clicked.connect(self.botao_grafico_processador)


    ##loop 
    def print_salvo_processador(self):

        self.LABEL_PRINT = QLabel(self)
        self.LABEL_PRINT.setText("SALVO")
        self.LABEL_PRINT.resize(130,30)
        self.LABEL_PRINT.setStyleSheet('QLabel{background-color: #1E90FF; font: italic;font-size: 25px}')# DodgerBlue
        self.LABEL_PRINT.setAlignment(QtCore.Qt.AlignCenter)
        self.LABEL_PRINT.show()

        if self.if_var == JANELA1:

            self.LABEL_PRINT.move(450,210)

        else:

            self.LABEL_PRINT.move(380,210)
            

    ##--------------------------------------------
    ## frame 6
    def whidget_configuracoes_6(self):

        self.botao_resert= QPushButton('RESERT',self)
        self.botao_resert.move(220,NUM20)#janela
        self.botao_resert.resize(NUM180,NUM40)
        self.botao_resert.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 18px}')#RED
        self.botao_resert.clicked.connect(self.if_de_processo_tb)
        self.botao_resert.show()

        self.LABEL_INF_RESERT = QLabel(self)
        self.LABEL_INF_RESERT.move(220,70)
        self.LABEL_INF_RESERT.setText("  * INICIA AS INFORMAÇÕES.")
        self.LABEL_INF_RESERT.resize(300,20)
        self.LABEL_INF_RESERT.setStyleSheet('QLabel{background-color: #00FF00; font: italic;font-size: 14px}')# 
        self.LABEL_INF_RESERT.show()
        
    
    def filtro_configuracoes_6(self):

        self.LABEL_FI = QLabel(self)
        self.LABEL_FI.move(210,330)
        self.LABEL_FI.resize(570,5)
        self.LABEL_FI.setStyleSheet('QLabel{background-color: #0000CD;}')# MediumBlue
        self.LABEL_FI.show()

        self.botao_ATESTAR= QPushButton('OK',self)
        self.botao_ATESTAR.move(600,340)#janela
        self.botao_ATESTAR.resize(NUM180,NUM40)
        self.botao_ATESTAR.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 20px}')#RED
        self.botao_ATESTAR.clicked.connect(self.funcao_conf_geral)
        self.botao_ATESTAR.show()

        self.botao_REJEITAR= QPushButton('CANCELAR',self)
        self.botao_REJEITAR.move(210,340)#janela
        self.botao_REJEITAR.resize(NUM180,NUM40)
        self.botao_REJEITAR.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 20px}')#RED
        self.botao_REJEITAR.clicked.connect(self.filtro_configuracoes_6_dest)
        self.botao_REJEITAR.show()

        
    ##--------------------------------------------
    ## frames and frames
    def whidget_frames_if (self):

        if self.whidget_dest == 0:

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

            self.whidget_dest = 1

    def whidget_frames_db_if(self):

        if self.whidget_frameeframe == 0:
            
            self.spin = QSpinBox(self)
            self.spin.move(220,210)
            self.spin.resize(100,30)
            self.spin.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
            self.spin.setMaximum(100)
            self.spin.setMinimum(1)
            self.spin.valueChanged.connect(self.widget_processador121)
            self.spin.show()

            self.whidget_frameeframe = 1

            self.QCB_C = QCheckBox("  ATIVAR CONTROLE",self)
            self.QCB_C.move(220,170)
            self.QCB_C.resize(250,30)
            self.QCB_C.setStyleSheet('QCheckBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
            self.QCB_C.stateChanged.connect(self.widget_processador12) 
            self.QCB_C.show()

        if self.whidget_frameeframe == 1 :
             self.desativar_QCB()
            
        if  self.if_var ==  JANELA2:
            self.spin_jan2_frameproc(NUMS2)

        elif self.if_var ==  JANELA3:
            self.spin_jan2_frameproc(NUMS3)

        elif self.if_var ==  JANELA5:
            self.spin_jan2_frameproc(NUMS1)
        
        
        
        




    


        

    
        

       
        
        
        
        