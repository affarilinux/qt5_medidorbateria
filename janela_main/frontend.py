from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel

class GuiFront(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        ## sistema fixo

        LABEL_MAIN_FIXO = QLabel(self)
        LABEL_MAIN_FIXO.setText("HARDWARE")
        LABEL_MAIN_FIXO.move(50,5)
        LABEL_MAIN_FIXO.resize(130,40)
        LABEL_MAIN_FIXO.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 20px}')# YELLOW

        LABEL_TRACO_FIXO = QLabel(self)
        LABEL_TRACO_FIXO.move(5,40)
        LABEL_TRACO_FIXO.resize(210,2)
        LABEL_TRACO_FIXO.setStyleSheet('QLabel{background-color: #FFFF00;}')
        

        self.BOTAO_APP= QPushButton('aplicativo',self)
        self.BOTAO_APP.move(10,350)#janela
        self.BOTAO_APP.resize(120,40)
        self.BOTAO_APP.setStyleSheet('QPushButton{background-color: #FFFF00; font: bold; font-size: 20px}')#Yellow


        self.BOTAO_SAIR = QPushButton('SAIR',self)
        self.BOTAO_SAIR.move(140,350)#janela
        self.BOTAO_SAIR.resize(70,40)
        self.BOTAO_SAIR.setStyleSheet('QPushButton{background-color: #FFFF00; font: italic; font-size: 20px}')# Yellow
        self.BOTAO_SAIR.clicked.connect(self.close)

        ## BATERIA

        LABEL_BATERIA_FIXO = QLabel(self)
        LABEL_BATERIA_FIXO.setText("BATERIA")
        LABEL_BATERIA_FIXO.move(70,55)
        LABEL_BATERIA_FIXO.resize(175,20)
        LABEL_BATERIA_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 20px}')# Lime

        casad = 100
        LABEL_100_VAR = QLabel(self)
        LABEL_100_VAR.setText("{} %".format(casad))
        LABEL_100_VAR.move(15,85)
        LABEL_100_VAR.resize(70,25)
        LABEL_100_VAR.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 18px}')# Lime

        LABEL_CARGA = QLabel(self)
        LABEL_CARGA.setText("DESCARREGADO")
        LABEL_CARGA.move(85,85)
        LABEL_CARGA.resize(125,25)
        LABEL_CARGA.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 13px}')# Lime
        
        ## traços

        LABEL_TRACO_FIXO1 = QLabel(self)
        LABEL_TRACO_FIXO1.move(5,110)
        LABEL_TRACO_FIXO1.resize(210,2)
        LABEL_TRACO_FIXO1.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        LABEL_TRACO_FIXO11 = QLabel(self)
        LABEL_TRACO_FIXO11.move(5,160)
        LABEL_TRACO_FIXO11.resize(210,2)
        LABEL_TRACO_FIXO11.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        LABEL_TRACO_FIXO12 = QLabel(self)
        LABEL_TRACO_FIXO12.move(5,230)
        LABEL_TRACO_FIXO12.resize(210,2)
        LABEL_TRACO_FIXO12.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        ## MEMORIA RAM

        LABEL_RAMNOME_FIXO = QLabel(self)
        LABEL_RAMNOME_FIXO.setText("RAM")
        LABEL_RAMNOME_FIXO.move(30,125)
        LABEL_RAMNOME_FIXO.resize(175,30)
        LABEL_RAMNOME_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 30px}')# Lime

        LABEL_100_VAR_RAM = QLabel(self)
        LABEL_100_VAR_RAM.setText("{} %".format(casad))
        LABEL_100_VAR_RAM.move(125,125)
        LABEL_100_VAR_RAM.resize(90,25)
        LABEL_100_VAR_RAM.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 25px}')# Lime

        ## temperatura média

        LABEL_TEMP_FIXO = QLabel(self)
        LABEL_TEMP_FIXO.setText("TEMPERATURA MÉDIA")
        LABEL_TEMP_FIXO.move(15,170)
        LABEL_TEMP_FIXO.resize(185,15)
        LABEL_TEMP_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 15px}')# Lime

        LABEL_100_VAR_TEMP = QLabel(self)
        LABEL_100_VAR_TEMP.setText("{} %".format(casad))
        LABEL_100_VAR_TEMP.move(70,195)
        LABEL_100_VAR_TEMP.resize(90,25)
        LABEL_100_VAR_TEMP.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 25px}')# Lime

        ## COOLER

        LABEL_COOLER_FIXO = QLabel(self)
        LABEL_COOLER_FIXO.setText("COOLER")
        LABEL_COOLER_FIXO.move(60,240)
        LABEL_COOLER_FIXO.resize(120,25)
        LABEL_COOLER_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 25px}')# Lime

        NOMED = "PROBLEMA"
        LABEL_COOLER_NOME = QLabel(self)
        LABEL_COOLER_NOME.setText("{}".format(NOMED))
        LABEL_COOLER_NOME.move(50,275)
        LABEL_COOLER_NOME.resize(130,20)
        LABEL_COOLER_NOME.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 20px}')# Lime
