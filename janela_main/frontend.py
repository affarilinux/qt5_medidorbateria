from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel

## EXTERNO PASTA
##CONFIGURACOES APP
from configuracoesapp.numero import (NUM2,NUM5,NUM15,NUM20,NUM25,NUM30,NUM40,NUM50,NUM70, NUM85,NUM90
                                    ,NUM120,NUM125,NUM130,NUM175,NUM210,
                                    NUM350)

class GuiFront(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        ## sistema fixo

        LABEL_MAIN_FIXO = QLabel(self)
        LABEL_MAIN_FIXO.setText("HARDWARE")
        LABEL_MAIN_FIXO.move(NUM50,NUM5)
        LABEL_MAIN_FIXO.resize(NUM130,NUM40)
        LABEL_MAIN_FIXO.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 20px}')# YELLOW

        LABEL_TRACO_FIXO = QLabel(self)
        LABEL_TRACO_FIXO.move(NUM5,NUM40)
        LABEL_TRACO_FIXO.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO.setStyleSheet('QLabel{background-color: #FFFF00;}')
        

        self.BOTAO_APP= QPushButton('aplicativo',self)
        self.BOTAO_APP.move(10,NUM350)#janela
        self.BOTAO_APP.resize(NUM120,NUM40)
        self.BOTAO_APP.setStyleSheet('QPushButton{background-color: #FFFF00; font: bold; font-size: 20px}')#Yellow


        self.BOTAO_SAIR = QPushButton('SAIR',self)
        self.BOTAO_SAIR.move(140,NUM350)#janela
        self.BOTAO_SAIR.resize(NUM70,NUM40)
        self.BOTAO_SAIR.setStyleSheet('QPushButton{background-color: #FFFF00; font: italic; font-size: 20px}')# Yellow
        self.BOTAO_SAIR.clicked.connect(self.close)

        ## BATERIA

        LABEL_BATERIA_FIXO = QLabel(self)
        LABEL_BATERIA_FIXO.setText("BATERIA")
        LABEL_BATERIA_FIXO.move(NUM70,55)
        LABEL_BATERIA_FIXO.resize(NUM175,NUM20)
        LABEL_BATERIA_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 20px}')# Lime

        casad = 100
        self.label_100_vav = QLabel(self)
        self.label_100_vav.move(NUM15,NUM85)
        self.label_100_vav.resize(NUM70,NUM25)
        self.label_100_vav.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 18px}')# Lime
        #@
        self.timer_bateria_100()

        self.label_carga = QLabel(self)
        self.label_carga.move(NUM85,NUM85)
        self.label_carga.resize(NUM125,NUM25)
        self.label_carga.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 13px}')# Lime
        #@
        self.timer_bateria_estado()
        ## traços

        LABEL_TRACO_FIXO1 = QLabel(self)
        LABEL_TRACO_FIXO1.move(NUM5,110)
        LABEL_TRACO_FIXO1.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO1.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        LABEL_TRACO_FIXO11 = QLabel(self)
        LABEL_TRACO_FIXO11.move(NUM5,160)
        LABEL_TRACO_FIXO11.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO11.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        LABEL_TRACO_FIXO12 = QLabel(self)
        LABEL_TRACO_FIXO12.move(NUM5,230)
        LABEL_TRACO_FIXO12.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO12.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        ## MEMORIA RAM

        LABEL_RAMNOME_FIXO = QLabel(self)
        LABEL_RAMNOME_FIXO.setText("RAM")
        LABEL_RAMNOME_FIXO.move(NUM30,NUM125)
        LABEL_RAMNOME_FIXO.resize(NUM175,NUM30)
        LABEL_RAMNOME_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 30px}')# Lime

        LABEL_100_VAR_RAM = QLabel(self)
        LABEL_100_VAR_RAM.setText("{} %".format(casad))
        LABEL_100_VAR_RAM.move(NUM125,NUM125)
        LABEL_100_VAR_RAM.resize(NUM90,NUM25)
        LABEL_100_VAR_RAM.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 25px}')# Lime

        ## temperatura média

        LABEL_TEMP_FIXO = QLabel(self)
        LABEL_TEMP_FIXO.setText("TEMPERATURA MÉDIA")
        LABEL_TEMP_FIXO.move(NUM15,170)
        LABEL_TEMP_FIXO.resize(185,NUM15)
        LABEL_TEMP_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 15px}')# Lime

        LABEL_100_VAR_TEMP = QLabel(self)
        LABEL_100_VAR_TEMP.setText("{} %".format(casad))
        LABEL_100_VAR_TEMP.move(NUM70,195)
        LABEL_100_VAR_TEMP.resize(NUM90,NUM25)
        LABEL_100_VAR_TEMP.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 25px}')# Lime

        ## COOLER

        LABEL_COOLER_FIXO = QLabel(self)
        LABEL_COOLER_FIXO.setText("COOLER")
        LABEL_COOLER_FIXO.move(60,240)
        LABEL_COOLER_FIXO.resize(NUM120,NUM25)
        LABEL_COOLER_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 25px}')# Lime

        NOMED = "PROBLEMA"
        LABEL_COOLER_NOME = QLabel(self)
        LABEL_COOLER_NOME.setText("{}".format(NOMED))
        LABEL_COOLER_NOME.move(NUM50,275)
        LABEL_COOLER_NOME.resize(NUM130,NUM20)
        LABEL_COOLER_NOME.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 20px}')# Lime
