        
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5.QtCore        import QTimer

'''
    CONFIGURACOES APP
'''
from configuracoesapp.string_letra import JANELA1,JANELA2,JANELA3,JANELA4,JANELA5,JANELA6
from configuracoesapp.numero import NUM0,NUM1

class Canva (QMainWindow ):    
     
    '''def Qtimer_canva_loop(self):
        
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
            QtCore.QTimer.singleShot(20000, self.Qtimer_canva_loop)


    def chart_graf(self):

        self.grafico = self.grafico +NUM1

        if self.grafico ==NUM1:

            self.umb()'''
    def button_lamda(self, ad):

        if ad == "a1":

            if self.entre_2 == 0:
                self.entre_2 = 1
                self.grafico_processador()

            elif self.entre_2 == 1:

                self.verificar_desativar_grafico()

            elif self.entre_2 == 2:

                self.verificar_desativar_grafico()

                self.entre_2 = 1
                self.grafico_processador()
        
        elif ad == "a2":

            if self.entre_2 == 0:
                self.entre_2 = 2
                self.grafico_processador()

            elif self.entre_2 == 1:

                self.verificar_desativar_grafico()

                self.entre_2 = 2
                self.grafico_processador()

            elif self.entre_2 == 2:

                self.verificar_desativar_grafico()  
        
            
    def grafico_processador(self):

        if self.qtimer_lop == 0:
            
            self.qtimer_lop = 1

            self.vericacao_org_grafico()


            self.qtimer_bateria1 = QTimer        ( self )

            self.qtimer_bateria1.setInterval     ( 10000 )
            self.qtimer_bateria1.start           ()

            #chamada de funçãO
            self.qtimer_bateria1.timeout.connect ( self.vericacao_org_grafico ) 

        else:
            
            self.verificar_desativar_grafico()

        
    def vericacao_org_grafico(self):

        if self.At_des== 0:
            
            self.single_ativar()
            self.At_des = 1

        else:
            self.single_desativar()
            

    def single_ativar(self):

        self.umb()

    def single_desativar(self):
                
        self.chart_delete()
        self.single_ativar()

    def variaveis_trabalho(self):

        self.qtimer_bateria1.stop()
        self.qtimer_lop = 0

        self.At_des= 0
        self.entre_2 = 0

        


           

       

        

        

   
