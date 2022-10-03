from PyQt5.QtWidgets import QMainWindow

class SecundariaApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.js = ChamarJanela()
        self.jt = JanelaTemporaria()
        
    
    def ativar_janela(self):
    
        self.js.show()

    def ativar_janela_temporaria(self):

        self.jt.show()

##-----------------------------------------------
                
'''
    APP2
'''
from APP_2.frondend2 import GUIFront2
from APP_2.destui_wii.destoiwidget import (DestWidget)
from APP_2.processo import Processo
from APP_2.canvas.ativadorgrap import Canva
from APP_2.funcao_front2 import Processo_front
from APP_2.canvas.grafico.tes import JanelaGrafico
from APP_2.button_state import EstadoBotoes

'''
    banco de dados
'''
from bancobd.jan_app.cooler_db1 import BancoCooler_p1
from bancobd.jan_app.close_app import BancoCloseApp
from bancobd.jan_app.graficodb import MostrarGrafico
from bancobd.jan_app.salvar_nivel import NivelJanela3

from bancobd.jan_db.apagarlinha  import ApagarTabela

from bancobd.db1 import Bancosqlite1

##################################################
class ChamarJanela(
    #APP2
    GUIFront2,DestWidget, Processo,Canva,
    Processo_front,JanelaGrafico, EstadoBotoes,
    #banco de dados
    Bancosqlite1, BancoCooler_p1,BancoCloseApp,
    MostrarGrafico,NivelJanela3,ApagarTabela,
    #meu grafico
    QMainWindow):

    def __init__(self):
        super(ChamarJanela, self).__init__()        

        self.setGeometry(600, 150, 800, 400) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#
        self.setWindowTitle("HARDWARE")


##------------------------------------------------
'''
    APP
'''
from APP3.frontend3 import FrontEnd3

'''
    BANCO
'''
from bancobd.db2 import BancoSqlite3

class JanelaTemporaria(
    #app
    FrontEnd3,
    #banco
    BancoSqlite3,
    QMainWindow):

     def __init__(self):
        super(JanelaTemporaria, self).__init__()        

        self.setGeometry(800,300,250,250) #j-XY app-XY
        self.setStyleSheet("background-color: #FF4500")#OrangeRed
        self.setWindowTitle("AVISO")


        


    

