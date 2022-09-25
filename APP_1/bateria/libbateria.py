import psutil

from PyQt5.QtWidgets import QMainWindow

'''
    CONFIGURACOES APP
'''
from configuracoesapp.letra import false_lt

class Bateria100(QMainWindow):
    
       
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
                
                aed = "00:00:00"
                
                self.label_carga.setText("CA: {}".format(aed))
                

          elif informacao_carregamento == false_lt :
                afe = "00:00:00"

                self.label_carga.setText( "DES: {}".format(afe))
                