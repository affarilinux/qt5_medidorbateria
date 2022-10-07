from PyQt5.QtWidgets import  QMainWindow

'''
    CONFIGURACOES APP
'''
from configuracoesapp.string_letra import (
    JANELA1, JANELA2,JANELA3,JANELA4,JANELA5,JANELA6,
    INI_LABEL,DESA_LABEL
    )
from configuracoesapp.numero import NUM1

class DestWidget(QMainWindow):

## ----------------------------------------------
## chamada
    def geral_destroi(self,des):

        if des == JANELA1:
            
            self.destif_janela5()

            self.LABEL_INFO_AVISO_BAT.deleteLater()
            self.LABEL_MIM_SPIN.deleteLater()
            self.LABEL_MAX_SPIN.deleteLater()
            self.spin_mim .deleteLater()
            self.spin_max.deleteLater()
            self.QCB_C_mm.setChecked( False )
            self.QCB_C_mm.deleteLater()

            self.botao_grap_bat_car.deleteLater()
            self.botao_grap_bat_des.deleteLater()
            
        elif des == JANELA2:
           
            self.destif_janela5()
            self.botao_grap_ram.deleteLater()
        
        elif des == JANELA3:
            
            self.LABEL_INFO_AVISO_IMP.deleteLater()
            self.botao_grap_tp.deleteLater()
            self.destif_janela5()
            
        elif des == JANELA4:

            self.LABEL_4x_COO.deleteLater()    
            self.destif_janela5()    

        elif des == JANELA5:
            
            self.verificar_desativar_grafico()
            self.botao_grap_p.deleteLater()
            
            self.destif_janela5()
            
        elif des == JANELA6:

            self.botao_resert.deleteLater()
            self.LABEL_INF_RESERT.deleteLater()

            if self.configuracoes_tb != None:
                self.filtro_configuracoes_6_dest()
                
            self.destif_janela5()
          

    ## -------------------------------------------
    ## funcoes

    def verificar_desativar_grafico(self):

        if self.At_des == 1:
                self.chart_delete()
                self.variaveis_trabalho()

    def chart_delete(self):
        
        self.chart.close()      

    def destif_janela5(self):

        if self.salvar_label == DESA_LABEL:
            self.LABEL_PRINT.deleteLater()

            self.qtimer_bateria1.stop()

            self.salvar_label = INI_LABEL

    def label_fixo_processo(self):

        if self.whidget_dest == 2:

            self.LABEL_AP.deleteLater()
            self.LABEL_LIN.deleteLater() 
            self.LABEL_INFO.deleteLater()
            self.LABEL_INFO_NUM.deleteLater()

            self.whidget_dest = 0

    def processo_spin_dest(self):

        if self.whidget_frameeframe == 2:
            self.desativar_QCB()
            self.QCB_C.deleteLater()
            self.spin.deleteLater()
          
            self.whidget_frameeframe =0

    def filtro_configuracoes_6_dest(self):

        self.LABEL_FI.deleteLater()
        self.botao_ATESTAR.deleteLater()
        self.botao_REJEITAR.deleteLater()
