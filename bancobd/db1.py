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

        self.if_var = None

    def if_var_var(self,processo_fram):
        self.if_var = processo_fram
        print(self.if_var)

    def chamar_banco(self):
        self.tarefa_cooler()

    def tarefa_cooler(self):
        if self.if_var == "janela4":
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

    def atual_frame_jan(self,proc):
        
        self.cursorsq.execute("SELECT * from COOLER WHERE id = ?",(NUMS1,))
        record = self.cursorsq.fetchone()
        if record == None:
            
            self.cursorsq.execute("INSERT INTO COOLER(id,estado_cooler) VALUES (?,?)",(NUMS1,proc))
            ##"INSERT INTO COOLER VALUES ('"++",'"++"')""

        elif record != None:
            
            self.cursorsq.execute("UPDATE COOLER SET estado_cooler = ?",(proc,))