import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import Qt

## sistema app
from janela_main.frontend import GuiFront

class Principal(GuiFront,QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()


        self.setAttribute(Qt.Qt.WA_TranslucentBackground, True )   
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, False)      
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setGeometry(1680, 100, 220, 400) #j-XY app-XY
        self.setStyleSheet("Principal{background-color: rgba(0,255,255, 30);}") #Aqua / Cyan

if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Principal()
    p.show()
    app.exec_()