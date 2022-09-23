'''
    configuracoes app
'''
from configuracoesapp.string_letra import JANELA4


class BancoCooler_p1:

    def chamar_banco(self):
        
        if self.if_var == JANELA4:
            self.tarefa_cooler()

    def tarefa_cooler(self):
        
        self.ativar_banco1()
        self.mostrar_cooler()
        self.sair_banco1()

    def mostrar_cooler(self):
        
       self.cur.execute("SELECT estado_cooler from COOLER")
       selec = self.cur.fetchone()
        
       for row  in selec:
            
            self.LABEL_4x_COO.setText(row)