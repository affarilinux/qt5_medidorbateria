import sqlite3
from PyQt5 import QtCore


'''
    CONFIGURACOES APP
'''
from configuracoesapp.numerostrig import NUMS1,NUMS2,NUMS3
from configuracoesapp.string_letra import PROCESSADOR,false_s,RAM_S,TEMPERATURA_S

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
        self.ler_text_2(NUMS2)
        self.ler_text_3(NUMS3)

        self.commit_banco2()
        self.sair_banco2()
    
        QtCore.QTimer.singleShot(3000, self.verificar_text_atlabelcor)

    def ler_text(self,Nt):

        self.cursort2.execute(
            """SELECT tipo_chamada from JANELA3 
            WHERE ID_JANELA = ?""",(Nt,))
        rec3t = self.cursort2.fetchone()

        if rec3t[0] == PROCESSADOR:

            self.LABEL3_PROC.setStyleSheet('QLabel{background-color: #00FF00;font: bold;font-size: 20px}')#
            self.cursort2.execute("UPDATE JANELA3 SET tipo_chamada= ? WHERE ID_JANELA = ?",(false_s,Nt))

        else:

            self.LABEL3_PROC.setText(PROCESSADOR)
            self.LABEL3_PROC.setStyleSheet('QLabel{background-color: #FF4500;font: bold;font-size: 20px}')#

    def ler_text_2(self,Nt_2):
    
        self.cursort2.execute(
            """SELECT tipo_chamada from JANELA3 
            WHERE ID_JANELA = ?""",(Nt_2,))
        rec3t_2 = self.cursort2.fetchone()

        if rec3t_2[0] == RAM_S:

            self.LABEL3_RAM.setStyleSheet('QLabel{background-color: #00FF00;font: bold;font-size: 20px}')# 
            self.cursort2.execute("UPDATE JANELA3 SET tipo_chamada = ? WHERE ID_JANELA = ?",(false_s,Nt_2))

        else:
            
            self.LABEL3_RAM.setText(RAM_S)
            self.LABEL3_RAM.setStyleSheet('QLabel{background-color: #FF4500;font: bold; font-size: 20px}')# 

    def ler_text_3(self,Nt_3):
    
        self.cursort2.execute(
            """SELECT tipo_chamada,qtd_valor from JANELA3 
            WHERE ID_JANELA = ?""",(Nt_3,))
        rec3t_3 = self.cursort2.fetchone()
        
        if (rec3t_3[0] == "FREQUÊNCIA" or rec3t_3[0] == "CORE" or
            rec3t_3[0] == "CORE1" or rec3t_3[0] =="core2" or 
            rec3t_3[0] =="WIFI"):
            
            SS = rec3t_3[0][0:5]
           
            self.LABEL3_TEMP.setStyleSheet('QLabel{background-color: #00FF00;font: bold;font-size: 20px}')#
            self.LABEL3_TEMP.setText("{} - {} °C".format (str(SS),str(rec3t_3[1])))
            self.cursort2.execute("UPDATE JANELA3 SET tipo_chamada = ?,qtd_valor = ? WHERE ID_JANELA = ?",(false_s, 0,Nt_3))

        else:

            self.LABEL3_TEMP.setText(TEMPERATURA_S)
            self.LABEL3_TEMP.setStyleSheet('QLabel{background-color: #FF4500;font: bold;font-size: 20px}')#
            
