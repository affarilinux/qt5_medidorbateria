from PyQt5.QtWidgets import QMainWindow

'''
    configuracoes app
'''
from configuracoesapp.string_letra import (
    true_s,JANELA4,JANELA5
    )

class BancoCloseApp(QMainWindow):

    def sair_app(self):

        self.ativar_banco1()
        self.analisar_banco()
        self.sair_banco1()

    def analisar_banco(self):

        self.cur.execute("SELECT fechar_janela from PROCESSOS_SISTEMA")
        selec_FV = self.cur.fetchone()
        
        for row_close  in selec_FV:

            if row_close == true_s:

                self.apagar_widget_banco()

    def apagar_widget_banco(self):

        if self.if_var == JANELA4:

            self.fechar_janela_secundaria()
        
        elif self.if_var == JANELA5:
            self.fechar_janela_secundaria()
            self.chart_delete()

    def fechar_janela_secundaria(self):

        self.close()
        
