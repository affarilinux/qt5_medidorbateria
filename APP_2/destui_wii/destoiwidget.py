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

    def geral_destroi(self,des):

        if des == JANELA1:
            self.dest_janela_1()

        elif des == JANELA2:
            self.dest_janela_2()
        
        elif des == JANELA3:
            self.dest_janela_3()
            
        elif des == JANELA4:
            self.dest_janela_4()

        elif des == JANELA5:
            self.dest_janela_5()

        elif des == JANELA6:
            self.dest_janela_6()

    def dest_janela_1(self):
        print(1111)

    def dest_janela_2(self):
        print(2222)

    def dest_janela_3(self):
        print(3333)
        
    def dest_janela_4(self):
        
        self.LABEL_4x_COO.deleteLater()

    def dest_janela_5(self):
        
        self.chart_delete()
        self.botao_grap_p.deleteLater()
        self.LABEL_AP.deleteLater()
        self.LABEL_LIN.deleteLater() 
        self.QCB_C.deleteLater()
        self.spin.deleteLater()
        self.LABEL_INFO.deleteLater()
        self.LABEL_INFO_NUM.deleteLater()

        if self.salvar_label == DESA_LABEL:
            self.destif_janela5()

    def dest_janela_6(self):
        
        self.botao_resert.deleteLater()
        self.LABEL_INF_RESERT.deleteLater()

    def chart_delete(self):
        
        if self.grafico ==NUM1:
            self.chart.close()      

    def destif_janela5(self):
        self.LABEL_PRINT.deleteLater()

        self.qtimer_bateria1.stop()

        self.salvar_label = INI_LABEL
