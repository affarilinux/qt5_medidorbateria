from PyQt5.QtWidgets import  QMainWindow

from configuracoesapp.string_letra import (JANELA1, JANELA2,JANELA3,
                                            JANELA4,JANELA5)

class DestWidget(QMainWindow):

    def geral_destroi(self,des):

        if des == JANELA1:
            self.dest_janela_1()

        elif des == JANELA2:
            self.dest_janela_2()
        
        elif des == JANELA3:
            self.dest_janela_3()
            
        elif des == JANELA4:
            self.dest_janela_4()

        elif des == JANELA5:
            self.dest_janela_5()

    def dest_janela_1(self):
        print(1111)

    def dest_janela_2(self):
        print(2222)

    def dest_janela_3(self):
        print(3333)
    def dest_janela_4(self):
        self.LABEL_4x_COO.deleteLater()

    def dest_janela_5(self):
        print(5555)