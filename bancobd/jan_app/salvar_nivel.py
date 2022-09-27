'''
    CONFIGURACOES app
'''
from configuracoesapp.numerostrig import NUMS1


class NivelJanela3:

    def spin_jan2_frameproc(self):
        
        self.ativar_banco1()

        self.cur.execute("SELECT   NIVEL_JANELA  from JANELA3 WHERE ID_JANELA = ?",(NUMS1,))
        spin_ler = self.cur.fetchone()

        for row_sp  in spin_ler:

             self.spin.setValue(row_sp)

        self.sair_banco1()
            
           
    def quantidade_banco_jan3(self,value_frame5):

        self.ativar_banco1()

        self.cur.execute("UPDATE JANELA3 SET NIVEL_JANELA  = ?",(value_frame5,))

        self.commit_banco1()
        self.sair_banco1()
