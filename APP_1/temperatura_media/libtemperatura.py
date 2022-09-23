import psutil

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore        import QTimer

'''
    CONFIGURACOES APP
'''
from configuracoesapp.numero import( 
    NUM0,NUM1,NUM2,NUM5
    )

class Temperatura100(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        qtimer_temperatura = QTimer        ( self )

        qtimer_temperatura.setInterval     ( 3000 )
        qtimer_temperatura.start           ()

        #chamada de funçãO
        qtimer_temperatura.timeout.connect ( self.temperatura_lib ) 

    def temperatura_lib(self):

        processador_temp = psutil.sensors_temperatures()['acpitz'][NUM0]

        core_temp        = psutil.sensors_temperatures()['coretemp'][NUM0]
        core_temp1       = psutil.sensors_temperatures()['coretemp'][NUM1]
        core_temp2       = psutil.sensors_temperatures()['coretemp'][NUM2]

        wifi_temp        = psutil.sensors_temperatures()['iwlwifi_1'][NUM0]

        processador_temp_cur = processador_temp.current

        core_temp_cur = core_temp.current
        core_temp1_cur = core_temp1.current
        core_temp2_cur = core_temp2.current

        wifi_temp_cur  = wifi_temp.current

        calculosoma = (processador_temp_cur + core_temp_cur + core_temp1_cur + 
                        core_temp2_cur + wifi_temp_cur ) / NUM5
        

        self.label_tempnum.setText("{} %".format(calculosoma))