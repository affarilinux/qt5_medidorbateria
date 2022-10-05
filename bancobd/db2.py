import sqlite3

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore        import QTimer

class Bancosqlite1(QMainWindow):
    def __init__( self ):
        
        super ().__init__() # metodo construtor

        qtimer_fans_p1 = QTimer        ( self )

        qtimer_fans_p1.setInterval     ( 10000 )
        qtimer_fans_p1.start           ()

        #chamada de funçãO
        qtimer_fans_p1.timeout.connect ( self.chamar_banco ) 

        ### --------------------------------------

        qtimer_loop_close = QTimer        ( self )

        qtimer_loop_close.setInterval     ( 2000 )
        qtimer_loop_close.start           ()

        #chamada de funçãO
        qtimer_loop_close.timeout.connect ( self.sair_app ) 

    ##
    def ativar_banco1(self):
        
        self.bancoco = sqlite3.connect('bancobd/banco_hard.db')

        self.cur = self.bancoco.cursor()

    def sair_banco1(self):
        self.cur.close()
        self.bancoco.close()

    def commit_banco1(self):
        self.bancoco.commit()
   
    

    