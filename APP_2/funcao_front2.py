'''
    CONFIGURACOES APP
'''
from configuracoesapp.string_letra import (
    JANELA1,JANELA2,JANELA3,JANELA4,JANELA5,
    INI_LABEL,DESA_LABEL
    )
from configuracoesapp.letra import true_lt
from configuracoesapp.numero import NUM0, NUM1

class Processo_front:

    def whidget_bateria (self):
    
        if self.if_var != JANELA1:

            self.geral_destroi(self.if_var)

            self.if_var = JANELA1

    def whidget_ram(self):

        if self.if_var != JANELA2:
    
            self.geral_destroi(self.if_var)

            self.if_var = JANELA2
            

    def whidget_temperatura(self):
    
        if self.if_var != JANELA3:
    
            self.geral_destroi(self.if_var)

            self.if_var = JANELA3

    def Whidget_cooler(self):
        
        if self.if_var != JANELA4:
            
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA4
            

        self.Whidget_cooler1()
        
        self.tarefa_cooler()

        self.estado_frame_false(self.if_var)

    ## ------------------------------------------
    #  processador
    def widget_processador(self):

        if self.if_var != JANELA5:
            
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA5
            
        #widget
        
        self.widget_processador1()

        self.estado_frame_false(self.if_var)
        
    
    def widget_processador121(self):
    
        if self.val == true_lt:
            value = self.spin.value()

            if self.salvar_label == INI_LABEL:
                self.print_salvo_processador()

                self.loop_frame_salvo()

                self.salvar_label = DESA_LABEL

    def botao_grafico_processador(self):

        if self.at_des_grafico == NUM0:
            self.at_des_grafico = NUM1
            if self.grafico == NUM0:
                self.grafico_processador()
            

        elif self.at_des_grafico == NUM1:
            self.at_des_grafico = NUM0
            if self.grafico == NUM1:
                self.chart_delete()
                self.grafico = NUM0


        