from PyQt5 import QtCore
from PyQt5.QtCore        import QTimer


'''
    configuracoes app
'''
from configuracoesapp.string_letra import JANELA1,INI_LABEL,DESA_LABEL
from configuracoesapp.letra import false_lt
from configuracoesapp.numero import NUM0,NUM5000


class Processo:
    def __init__( self ):
        
        super ().__init__() # metodo construtor
        self.if_var = JANELA1
        self.val = false_lt
        self.salvar_label = INI_LABEL
        self.whidget_dest = 0
        self.whidget_frameeframe = 0
        self.configuracoes_tb = None
        self.val_bat = false_lt

        self.qtimer_lop = 0
        self.At_des     = 0
        
    def widget_processador12(self,state):
    
        self.val = state == QtCore.Qt.Checked
              
        self.widget_processador121()

    def whidget_bateria_val(self, state_pi):

        self.val_bat = state_pi == QtCore.Qt.Checked
        
        self.if_qcb_batval()

    def qtimer_loop_salvar(self):

        self.print_salvo_processador()

        self.qtimer_bateria1 = QTimer        ( self )

        self.qtimer_bateria1.setInterval     ( NUM5000 )
        self.qtimer_bateria1.start           ()

        #chamada de funçãO
        self.qtimer_bateria1.timeout.connect ( self.destif_janela5 ) 

        self.salvar_label = DESA_LABEL

   