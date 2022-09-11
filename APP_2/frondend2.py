from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import QtCore 

## EXTERNO PASTA
##CONFIGURACOES APP
from configuracoesapp.numero import ( NUM5,NUM10,NUM20,
                                    NUM40,NUM100
                                    ,NUM140,NUM180,
                                    NUM200)


from bancobd.db1 import Bancosqlite1
class GUIFront2(Bancosqlite1,QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        # frame janela

        LABEL2_JANERLA = QLabel(self)
        LABEL2_JANERLA.move(NUM5,NUM10)
        LABEL2_JANERLA.resize(190,780)
        LABEL2_JANERLA.setStyleSheet('QLabel{background-color: #FFFF00;}')# YELLOW

        self.botao2_janela= QPushButton('BATERIA',self)
        self.botao2_janela.move(NUM10,NUM20)#janela
        self.botao2_janela.resize(NUM180,NUM40)
        self.botao2_janela.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 20px}')#RED
        #self.botao2_janela.clicked.connect(self.ativar_janela)

        self.botao2_janela2= QPushButton('RAM',self)
        self.botao2_janela2.move(NUM10,80)#janela
        self.botao2_janela2.resize(NUM180,NUM40)
        self.botao2_janela2.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 20px}')#RED
        #self.botao2_janela2.clicked.connect(self.ativar_janela)

        self.botao2_janela3= QPushButton('TEMPORATURA',self)
        self.botao2_janela3.move(NUM10,NUM140)#janela
        self.botao2_janela3.resize(NUM180,NUM40)
        self.botao2_janela3.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 20px}')#RED
        #self.botao2_janela3.clicked.connect(self.ativar_janela)

        self.botao2_janela4= QPushButton('COOLER',self)
        self.botao2_janela4.move(NUM10,NUM200)#janela
        self.botao2_janela4.resize(NUM180,NUM40)
        self.botao2_janela4.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 20px}')#RED
        self.botao2_janela4.clicked.connect(self.Whidget_cooler)

        self.botao2_janela5= QPushButton('PROCESSADOR',self)
        self.botao2_janela5.move(NUM10,260)#janela
        self.botao2_janela5.resize(NUM180,NUM40)
        self.botao2_janela5.setStyleSheet('QPushButton{background-color: #FF0000; font: bold; font-size: 20px}')#RED
        #self.botao2_janela5.clicked.connect(self.asd)
   
    def Whidget_cooler(self):
        
        self.LABEL_4x_COO = QLabel(self)
        self.LABEL_4x_COO.move(NUM200,300)
        self.LABEL_4x_COO.resize(900,NUM100)
        self.LABEL_4x_COO.setStyleSheet('QLabel{background-color: #FF00FF;font: bold; font-size: 60px}')# 
        self.LABEL_4x_COO.setAlignment(QtCore.Qt.AlignCenter)
        self.LABEL_4x_COO.show()

        self.tarefa_cooler()


        

    '''def asd(self):
        self.LABEL_4x_COO.deleteLater()'''

       
        
        
        
        