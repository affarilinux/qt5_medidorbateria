import psutil

from PyQt5.QtWidgets import QMainWindow

'''
    CONFIGURACOES APP
'''
from configuracoesapp.numero import (
    NUM2,NUM100
    )

class Ram100(QMainWindow):
   
    def  memoria_ram( self ):
    
        #informações da memoria ram
        informacao           = psutil.virtual_memory ()

        # puxa as informações e adiciona nas variaveis
        total                = informacao.total
        usada                = informacao.active

        # calcula porcentagm
        calculo_por_centagem      = ( usada * NUM100 ) / total

        # filtra o float
        calculo_filtro_informacao = round ( calculo_por_centagem, NUM2 )

        self.label_100_vav_ram.setText("{} %".format(calculo_filtro_informacao))

        self.ativar_janela_ram(calculo_filtro_informacao)