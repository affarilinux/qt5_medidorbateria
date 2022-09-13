from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore        import QTimer

from APP_2.canvas.grafico.ext_processador import Canvas

class Canva (QMainWindow):

    def __init__(self):
        super().__init__()

        '''qtimer_canva = QTimer        ( self )

        qtimer_canva.setInterval     ( 60000 )
        qtimer_canva.start           ()

        #chamada de funçãO
        qtimer_canva.timeout.connect ( self.grafico_processador ) '''

        
    def grafico_processador(self):
        
        self.chart = Canvas(self)
        self.chart.move(210,10)
        self.chart. resize(960,500)
        
        self.chart.show()

    def apagar(self):
        self.chart.deleteLater()
