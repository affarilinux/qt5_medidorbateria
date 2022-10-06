from PyQt5 import QtCore
'''
    configuracoes app
'''
from configuracoesapp.string_letra import BATERIA_S
class ProcessoBateria:

    def __init__( self ):
        
        super ().__init__() # metodo construtor

        self.loop_spi = 0

    def salvar_spinbateria(self,mim,max):

        if max>mim:
            
            self.ativar_banco1()
            
            self.cur.execute(
                "UPDATE  JANELA3 SET tipo_chamada = ?,NIVEL_JANELA =?,qtd_valor=?  where ID_JANELA = ?",(BATERIA_S,mim,max,4))
            
            
            self.commit_banco1()
            self.sair_banco1()

        else:

            if self.loop_spi == 0:
                
                self.loop_spi =1
                QtCore.QTimer.singleShot(4000, self.mostrar_spin_bateria)

    def mostrar_spin_bateria(self):

        self.ativar_banco1()

        self.cur.execute("SELECT NIVEL_JANELA,qtd_valor from  JANELA3  WHERE ID_JANELA = ?", (4,))
        jan4_valor = self.cur.fetchone()

        self.spin_mim.setValue(jan4_valor[0])
        self.spin_max.setValue(jan4_valor[1])

        self.bancoco.close()

        self.loop_spi = 0


