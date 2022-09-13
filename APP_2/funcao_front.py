
from configuracoesapp.string_letra import (JANELA1,JANELA2,JANELA3,
                                        JANELA4,JANELA5)

class Processo_front:

    def whidget_bateria (self):
    
        if self.if_var != JANELA1:

            self.geral_destroi(self.if_var)

            self.if_var_var(JANELA1)
        ##widget

        
        ##tarefa

    def whidget_ram(self):

        if self.if_var != JANELA2:
    
            self.geral_destroi(self.if_var)

            self.if_var_var(JANELA2)

    def whidget_temperatura(self):
    
        if self.if_var != JANELA3:
    
            self.geral_destroi(self.if_var)

            self.if_var_var(JANELA3)

    def Whidget_cooler(self):
        
        if self.if_var != JANELA4:

            self.geral_destroi(self.if_var)

            self.if_var_var(JANELA4)

        self.Whidget_cooler1()
        
        self.tarefa_cooler()


    def widget_processador(self):

        if self.if_var != JANELA5:
            
            self.geral_destroi(self.if_var)

            self.if_var_var(JANELA5)

        self.grafico_processador()