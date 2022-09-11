import sqlite3

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore        import QTimer

from configuracoesapp.numerostrig import NUMS1

class Bancosqlite1(QMainWindow):
    def __init__( self ):
        
        super ().__init__() # metodo construtor

        qtimer_fans = QTimer        ( self )

        qtimer_fans.setInterval     ( 10000 )
        qtimer_fans.start           ()

        #chamada de funçãO
        qtimer_fans.timeout.connect ( self.chamar_banco ) 
    
    def chamar_banco(self):
        self.tarefa_cooler()

    def tarefa_cooler(self):
        self.ativar_banco1()
        self.mostrar_cooler()
        self.sair_banco1()
    ##
    def ativar_banco1(self):
        self.bancoco = sqlite3.connect('bancobd/banco_hard.db')

        self.cur = self.bancoco.cursor()

    def sair_banco1(self):
        self.cur.close()
        self.bancoco.close()

    def commit_banco1(self):
        self.bancoco.commit()
   
    def mostrar_cooler(self):
        
        self.cur.execute("SELECT estado_cooler from COOLER")
        selec = self.cur.fetchone()
        
        for row  in selec:
            
            self.LABEL_4x_COO.setText(row)