import psutil

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore        import QTimer

'''
    CONFIGURACOES APP
'''
from configuracoesapp.numero import (
    NUM2,NUM100, NUM5000
    )

class Ram100(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        qtimer_ram = QTimer        ( self )

        qtimer_ram.setInterval     ( NUM5000 )
        qtimer_ram.start           ()

        #chamada de funçãO
        qtimer_ram.timeout.connect ( self.memoria_ram ) 

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