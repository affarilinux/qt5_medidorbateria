import psutil

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore        import QTimer

class CoolerAtivo(QMainWindow):
    
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        qtimer_fans = QTimer        ( self )

        qtimer_fans.setInterval     ( 100000 )
        qtimer_fans.start           ()

        #chamada de funçãO
        qtimer_fans.timeout.connect ( self.leitura_fans ) 

    def leitura_fans(self):
        fans_leiint = psutil.sensors_fans()
        fans_sis = None
        #print(fans_sis)

        if not fans_leiint:
            fans_sis = "SEM INFORMAÇÃO"

            self.label_cooler_nome.setText("{}".format(fans_sis))

        else:
            self.label_cooler_nome.setText("{}".format('INFORMAÇÃO'))

        #print(fans_sis)