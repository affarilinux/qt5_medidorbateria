from PyQt5.QtWidgets import QMainWindow


class SecundariaApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.js = ChamarJanela()
    
    def ativar_janela(self):
    
        self.js.show()


from APP_2.frondend2 import GUIFront2
##################################################
class ChamarJanela(GUIFront2,
                    QMainWindow):
    def __init__(self):
        super(ChamarJanela, self).__init__()        

        self.setGeometry(400, 150, 1200, 800) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#PowderBlue


    

