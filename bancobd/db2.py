import sqlite3

'''
    CONFIGURACOES APP
'''
from configuracoesapp.numerostrig import NUMS1
from configuracoesapp.string_letra import PROCESSADOR,false_s

class BancoSqlite3:

    def ativar_banco2(self):
        
        self.bancot22 = sqlite3.connect('bancobd/banco_hard.db')

        self.cursort2 = self.bancot22.cursor()

    
    def commit_banco2(self):
        self.bancot22.commit()

    def sair_banco2(self):
        self.cursort2.close()
        self.bancot22.close()


    def verificar_text_atlabelcor(self):

        self.ativar_banco2()

        self.ler_text(NUMS1)

        self.sair_banco2()
    

    def ler_text(self,Nt):

        self.cursort2.execute(
            """SELECT tipo_chamada from JANELA3 
            WHERE ID_JANELA = ?""",(Nt,))
        rec3t = self.cursort2.fetchone()

        if rec3t == PROCESSADOR:

            self.LABEL3_PROC.setStyleSheet('QLabel{background-color: #00FF00;}')#
            self.cursort2.execute("UPDATE JANELA3 SET NIVEL_JANELA = ?",(false_s,))