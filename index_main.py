import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import Qt

## sistema app
##pasta bateria
from bateria.libbateria import Bateria100
##pasta janela main
from janela_main.frontend import GuiFront
##processador
from processador.libprocessador import Processador100
## pasta ram
from RAM.libram import Ram100
## temperatura hardware
from temperatura_media.libtemperatura import Temperatura100
##cooler
from cooler.libcooler import CoolerAtivo

class Principal( Bateria100,
                GuiFront,
                Processador100,
                Ram100,
                Temperatura100,
                CoolerAtivo,
                QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()


        self.setAttribute(Qt.Qt.WA_TranslucentBackground, True )   
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, False)      
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setGeometry(1680, 100, 220, 430) #j-XY app-XY
        self.setStyleSheet("Principal{background-color: rgba(0,255,255, 30);}") #Aqua / Cyan

if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Principal()
    p.show()
    app.exec_()