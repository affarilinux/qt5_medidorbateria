from PyQt5.QtWidgets import QMainWindow

'''
    CONFIGURACOES APP
'''
from configuracoesapp.string_letra import JANELA4,JANELA5
from configuracoesapp.letra        import false_lt,true_lt

class EstadoBotoes (QMainWindow):

    def estado_frame_true(self,state_t):

        if state_t == JANELA4:
            self.botao2_janela4.setEnabled(true_lt)

        elif state_t == JANELA5:
            self.botao2_janela5.setEnabled(true_lt)

    def estado_frame_false(self,state_f):

        if state_f == JANELA4:
            self.botao2_janela4.setEnabled(false_lt)

        elif state_f == JANELA5:
            self.botao2_janela5.setEnabled(false_lt)

