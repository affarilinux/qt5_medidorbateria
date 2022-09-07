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

        if not fans_leiint:
            self.label_cooler_nome.setText("{}".format('not'))

        else:
            self.label_cooler_nome.setText("{}".format('yes'))