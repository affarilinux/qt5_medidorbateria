
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
        
        self.if_QCB_spin()

        ## whidget
        self.whidget_frames_if()
        self.Whidget_BATERIA()
       
        self.mostrar_spin_bateria()
        ##estado
        self.estado_frame_false(self.if_var)

    def whidget_ram_fun(self):

        if self.if_var != JANELA2:
    
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA2

        self.label_fixo_processo()

        self.whidget_frames_db_if()

        self.whidget_frames_if()
        ##widget
        self.whidget_ram()

        self.estado_frame_false(self.if_var)
            

    def whidget_temperatura(self):
    
        if self.if_var != JANELA3:
    
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA3

        self.label_fixo_processo()
        
        self.whidget_frames_db_if()
        self.whidget_frames_if()
        # WIDGET
        self.Whidget_TEMPERATURA()
        self.estado_frame_false(self.if_var)

    def Whidget_cooler(self):
        
        if self.if_var != JANELA4:
            
            self.geral_destroi(self.if_var)
            self.estado_frame_true(self.if_var)

            self.if_var = JANELA4
        
        if self.whidget_dest ==1:
            self.whidget_dest = 2
            self.label_fixo_processo()

        self.if_QCB_spin()

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
        
        self.if_QCB_spin()

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
                
                self.qtimer_loop_salvar()
               
    ##--------------------------------------------
    ##bateria
    def if_qcb_batval(self):
        
        if self.val_bat == true_lt:

            value_mim = self.spin_mim.value()
            value_max = self.spin_max.value()
            
            self.salvar_spinbateria(value_mim,value_max)

            if self.salvar_label == INI_LABEL:
                
                self.qtimer_loop_salvar()

    ##--------------------------------------------
    ## configuracoes 6
    def if_de_processo_tb (self):
            self.configuracoes_tb = 0

            self.filtro_configuracoes_6()

    def funcao_conf_geral(self):
       
        if self.configuracoes_tb ==0:
            self.apagar_registro()

    def if_QCB_spin(self):

        if self.whidget_frameeframe == 1:
            self.whidget_frameeframe =2
            self.processo_spin_dest()

    def desativar_QCB(self):
        self.QCB_C.setChecked( False )






        
            

        