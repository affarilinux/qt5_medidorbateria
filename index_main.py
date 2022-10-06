import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import Qt

'''
    APP1
'''
from APP_1.bateria.libbateria import Bateria100
##pasta janela main
from APP_1.frontend import GuiFront
##processador
from APP_1.processador.libprocessador import Processador100
## pasta ram
from APP_1.RAM.libram import Ram100
## temperatura hardware
from APP_1.temperatura_media.libtemperatura import Temperatura100
##cooler
from APP_1.cooler.libcooler import CoolerAtivo  

'''
    janela_aplicativo
'''
from janela_aplicativo.janela_app import SecundariaApp
from janela_aplicativo.inter_janela.processop1 import ProcessoJanela1

'''
    banco de dados
'''
from bancobd.db import Bancosqlite
from bancobd.jan_db.cooler_db import BancoCooler
from bancobd.jan_db.banco_salvar import SalvarProcessador
from bancobd.jan_db.data_bd_p import DataAtual
from bancobd.jan_db.ativar_jan3db import AtivarJanela3
from bancobd.jan_db.bateria_db import BateriaJan1

'''
    configuracoes app
'''
from configuracoesapp.letra import false_lt,true_lt

class Principal(
    #app1
    Bateria100,GuiFront,Processador100,Ram100,
    Temperatura100,CoolerAtivo,
    #janela aplicatico
    SecundariaApp,ProcessoJanela1,
    #banco de dados
    Bancosqlite,BancoCooler,SalvarProcessador,
    DataAtual,AtivarJanela3,BateriaJan1,
    #minha janela
    QMainWindow):

    def __init__(self):
        super(Principal, self).__init__()

        self.setAttribute(Qt.Qt.WA_TranslucentBackground, true_lt )   
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, false_lt)      
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setGeometry(1680, 100, 220, 430) #j-XY app-XY
        self.setStyleSheet("Principal{background-color: rgba(0,255,255, 30);}") #Aqua / Cyan


if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Principal()
    p.show()
    app.exec_()


