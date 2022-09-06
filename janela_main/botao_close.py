from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel

class BotaoSairMain(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        LABEL_MAIN_FIXO = QLabel(self)
        LABEL_MAIN_FIXO.setText("HARDWARE")
        LABEL_MAIN_FIXO.move(50,5)
        LABEL_MAIN_FIXO.resize(130,40)
        LABEL_MAIN_FIXO.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 20px}')
        

        self.BOTAO_APP= QPushButton('aplicativo',self)
        self.BOTAO_APP.move(10,350)#janela
        self.BOTAO_APP.resize(120,40)
        self.BOTAO_APP.setStyleSheet('QPushButton{background-color: #FFFF00; font: bold; font-size: 20px}')#Yellow


        self.BOTAO_SAIR = QPushButton('SAIR',self)
        self.BOTAO_SAIR.move(140,350)#janela
        self.BOTAO_SAIR.resize(70,40)
        self.BOTAO_SAIR.setStyleSheet('QPushButton{background-color: #FFFF00; font: italic; font-size: 20px}')# Yellow
        self.BOTAO_SAIR.clicked.connect(self.close)