from PyQt5 import QtCore
from PyQt5.QtCore        import QTimer

'''
    configuracoes app
'''
from configuracoesapp.string_letra import JANELA1,INI_LABEL
from configuracoesapp.letra import false_lt
from configuracoesapp.numero import NUM0,NUM5000


class Processo:
    def __init__( self ):
        
        super ().__init__() # metodo construtor
        self.if_var = JANELA1
        self.val = false_lt
        self.salvar_label = INI_LABEL
        self.grafico = NUM0
        self.at_des_grafico = NUM0
        self.loop_qtimer = NUM0
        
    def widget_processador12(self,state):
    
        self.val = state == QtCore.Qt.Checked
       
        print(str(self.val))
        
        self.widget_processador121()

    def loop_frame_salvo(self):
            self.qtimer_bateria1 = QTimer        ( self )

            self.qtimer_bateria1.setInterval     ( NUM5000 )
            self.qtimer_bateria1.start      ()

        #chamada de funçãO
            self.qtimer_bateria1.timeout.connect ( self.destif_janela5 )

   