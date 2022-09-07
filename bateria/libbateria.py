import psutil

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore        import QTimer

## EXTERNO
from configuracoesapp.numero import NUM5000

class Bateria100(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        qtimer_bateria = QTimer        ( self )

        qtimer_bateria.setInterval     ( NUM5000 )
        qtimer_bateria.start           ()

        #chamada de funçãO
        qtimer_bateria.timeout.connect ( self.chamada_qtimerbateria ) 
    
    def chamada_qtimerbateria(self):
        self.timer_bateria_100()
        self.timer_bateria_estado()

        ##100%
    def timer_bateria_100( self ):
    
        # chama os dados para a janela
        BATERIA_sistema = psutil.sensors_battery()

        # chama o tipo de informação
        nivel_bateria   = BATERIA_sistema.percent

        # transforma em int
        entrada_informacao = int(nivel_bateria)

        

        self.label_100_vav.setText("{} %".format(entrada_informacao))

        ##estado da bateria
    def timer_bateria_estado( self ):
    
          # puxa os dado do sistema operacional
          informacao_bateria = psutil.sensors_battery()

          # puxa uma informação se esta plugado na internet
          informacao_carregamento = informacao_bateria.power_plugged      

          if informacao_carregamento   == True :
                self.label_carga.setText("CARREGADO")
                

          elif informacao_carregamento == False :

                self.label_carga.setText("DESCARREGADO")
                