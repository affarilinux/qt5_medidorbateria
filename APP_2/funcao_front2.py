from PyQt5.QtCore        import QTimer

'''
    CONFIGURACOES APP
'''
from configuracoesapp.string_letra import (
    JANELA1,JANELA2,JANELA3,JANELA4,JANELA5,JANELA6,
    INI_LABEL,DESA_LABEL
    )
from configuracoesapp.letra import true_lt
from configuracoesapp.numero import NUM0, NUM1,NUM5000

class Processo_front:

##------------------------------------------------
## frames

    def whidget_bateria (self):
    
        ## destroi
        if self.if_var != JANELA1:

            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA1

        self.label_fixo_processo()

        if self.whidget_frameeframe == 1:
            self.whidget_frameeframe =2
            self.processo_spin_dest()

        ## whidget
        self.whidget_frames_if()
        ##estado
        self.estado_frame_false(self.if_var)

    def whidget_ram(self):

        if self.if_var != JANELA2:
    
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA2
        self.label_fixo_processo()

        self.whidget_frames_db_if()

        self.whidget_frames_if()

        self.estado_frame_false(self.if_var)
            

    def whidget_temperatura(self):
    
        if self.if_var != JANELA3:
    
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA3
        self.label_fixo_processo()
        
        self.whidget_frames_db_if()
        self.whidget_frames_if()
        self.estado_frame_false(self.if_var)

    def Whidget_cooler(self):
        
        if self.if_var != JANELA4:
            
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA4
        
        if self.whidget_dest ==1:
            self.whidget_dest = 2
            self.label_fixo_processo()

        if self.whidget_frameeframe == 1:
            self.whidget_frameeframe =2
            self.processo_spin_dest()

        self.Whidget_cooler1()
        
        self.tarefa_cooler()

        
        self.estado_frame_false(self.if_var)

    
    #  processador
    def widget_processador(self):

        if self.if_var != JANELA5:
            
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA5
            
        #widget
        self.label_fixo_processo()

        self.widget_processador1()

        self.whidget_frames_if()

        self.whidget_frames_db_if()

        self.estado_frame_false(self.if_var)
        
    
    def whidget_configuracoes(self):
    
        if self.if_var != JANELA6:
            
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA6
        if self.whidget_dest ==1:
            self.whidget_dest = 2
            self.label_fixo_processo()
        
        if self.whidget_frameeframe == 1:
            self.whidget_frameeframe =2
            self.processo_spin_dest()

        self.whidget_configuracoes_6()

        self.estado_frame_false(self.if_var)

    ###-------------------------------------------
    ##loop
    def widget_processador121(self):
    
        if self.val == true_lt:

            value = self.spin.value()

            if self.if_var == JANELA2:
                self.quantidade_banco_jan3(value,2)
                
            elif self.if_var == JANELA3:
                self.quantidade_banco_jan3(value,3)

            elif self.if_var == JANELA5:
                self.quantidade_banco_jan3(value,1)

            if self.salvar_label == INI_LABEL:
                self.print_salvo_processador()

                self.qtimer_bateria1 = QTimer        ( self )

                self.qtimer_bateria1.setInterval     ( NUM5000 )
                self.qtimer_bateria1.start           ()

                #chamada de funçãO
                self.qtimer_bateria1.timeout.connect ( self.destif_janela5 ) 

                self.salvar_label = DESA_LABEL
               
        
    ##--------------------------------------------
    ## botao grafico
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



        
            

        