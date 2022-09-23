        
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore

'''
    CONFIGURACOES APP
'''
from configuracoesapp.string_letra import JANELA4,JANELA5
from configuracoesapp.numero import NUM0,NUM1

class Canva (QMainWindow ):    
     
    def Qtimer_canva_loop(self):
        
        if self.if_var == JANELA4:

            self.grafico = NUM0

        elif self.if_var == JANELA5:
            
            if self.at_des_grafico == NUM1:
                self.chart_delete()
            self.grafico = NUM0
            self.loop_qtimer = NUM0
           
        QtCore.QTimer.singleShot(1000, self.grafico_processador)
            
    def grafico_processador(self):

        if self.if_var == JANELA4:

            self.grafico = NUM0
         
        elif self.if_var == JANELA5:

            if self.at_des_grafico == NUM1:
                            
                self.chart_graf()

        self.loop_qtimer = self.loop_qtimer +NUM1
        if self.loop_qtimer == NUM1:
            QtCore.QTimer.singleShot(15000, self.Qtimer_canva_loop)


    def chart_graf(self):

        self.grafico = self.grafico +NUM1

        if self.grafico ==NUM1:

            self.umb()

            
        
        
       

        

        

   
