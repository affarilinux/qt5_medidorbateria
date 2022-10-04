from PyQt5.QtWidgets import QMainWindow

'''
    CONFIGURACOES APP
'''
from configuracoesapp.string_letra import JANELA1,JANELA2,JANELA3,JANELA4,JANELA5,JANELA6
from configuracoesapp.letra        import false_lt,true_lt

class EstadoBotoes (QMainWindow):

    def estado_frame_true(self,state_t):

        if state_t == JANELA1:
            self.botao2_janela.setEnabled(true_lt)
        
        elif state_t == JANELA2:
            self.botao2_janela2.setEnabled(true_lt)
        
        elif state_t == JANELA3:
            self.botao2_janela3.setEnabled(true_lt)

        elif state_t == JANELA4:
            self.botao2_janela4.setEnabled(true_lt)

        elif state_t == JANELA5:
            self.botao2_janela5.setEnabled(true_lt)

        elif state_t == JANELA6:
            self.botao2_conf.setEnabled(true_lt)
            

    def estado_frame_false(self,state_f):

        if state_f == JANELA1:
            self.botao2_janela.setEnabled(false_lt)

        elif state_f == JANELA2:
            self.botao2_janela2.setEnabled(false_lt)

        elif state_f == JANELA3:
            self.botao2_janela3.setEnabled(false_lt)

        elif state_f == JANELA4:
            self.botao2_janela4.setEnabled(false_lt)

        elif state_f == JANELA5:
            self.botao2_janela5.setEnabled(false_lt)
        
        elif state_f == JANELA6:
            self.botao2_conf.setEnabled(false_lt)

