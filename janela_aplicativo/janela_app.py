from PyQt5.QtWidgets import QMainWindow


class SecundariaApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.js = ChamarJanela()
    
    def ativar_janela(self):
    
        self.js.show()
        

from APP_2.frondend2 import GUIFront2
from APP_2.destui_wii.destoiwidget import (DestWidget)
from bancobd.db1 import Bancosqlite1
from APP_2.processo import Processo
from APP_2.canvas.ativadorgrap import Canva
from APP_2.funcao_front import Processo_front
##################################################
class ChamarJanela(GUIFront2,
                    DestWidget,
                    Bancosqlite1,
                    Processo,
                    Canva,Processo_front,
                    QMainWindow):
    def __init__(self):
        super(ChamarJanela, self).__init__()        

        self.setGeometry(400, 150, 1200, 800) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#PowderBlue


    

