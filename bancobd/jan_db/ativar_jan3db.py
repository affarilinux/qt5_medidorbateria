
'''
    CONFIGURACOES APP
'''
from configuracoesapp.numerostrig import NUMS1
from configuracoesapp.string_letra import PROCESSADOR
class AtivarJanela3:

    def ativar_janela_processador(self,num_proc):

        self.ativar_banco()

        self.cursorsq.execute("SELECT NIVEL_JANELA from JANELA3 WHERE ID_JANELA = ?",(NUMS1,))
        jan_proc3 = self.cursorsq.fetchone()

        for row_at3 in jan_proc3:
        
            if num_proc >= row_at3:

                self.ativar_janela_temporaria()

                self.cursorsq.execute("UPDATE JANELA3 SET NIVEL_JANELA = ?",(PROCESSADOR,))
                

        self.sair_banco()