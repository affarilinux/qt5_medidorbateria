import psutil

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore        import QTimer

## EXTERNO
from configuracoesapp.numero import NUM2,NUM100, NUM5000

class Processador100(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        qtimer_ram = QTimer        ( self )

        qtimer_ram.setInterval     ( NUM5000 )
        qtimer_ram.start           ()

        #chamada de funçãO
        qtimer_ram.timeout.connect ( self.processador_frequencia ) 

    def processador_frequencia ( self ):
    
        # chama os dados para a janela
        informacao_sistema_1 = psutil.cpu_freq ()

        # puxa as informações e adiciona nas variaveis
        maximo_processador   = informacao_sistema_1.max
        dados_presente       = informacao_sistema_1.current

         # calcula porcentagm
        calculo_processos_dados     = ( dados_presente * NUM100 ) / maximo_processador

        # filtra o float
        filtra_calculo_sistema = round ( calculo_processos_dados, NUM2 )

        self.label_100_vav_proc.setText("{} %".format(filtra_calculo_sistema))
        