import psutil

from PyQt5.QtWidgets import QMainWindow

'''
    CONFIGURACOES APP
'''
from configuracoesapp.numero import (
    NUM2,NUM100
    )

class Processador100(QMainWindow):
    
    def processador_frequencia ( self ):
    
        # chama os dados para a janela
        informacao_sistema_1 = psutil.cpu_freq ()

        # puxa as informações e adiciona nas variaveis
        maximo_processador   = informacao_sistema_1.max
        dados_presente       = informacao_sistema_1.current

         # calcula porcentagm
        calculo_processos_dados     = ( dados_presente * NUM100 ) / maximo_processador

        # filtra o float
        self.filtra_calculo_sistema = round ( calculo_processos_dados, NUM2 )

        self.label_100_vav_proc.setText("{} %".format(self.filtra_calculo_sistema))

        self.ativar_janela_processador(self.filtra_calculo_sistema)

       
        