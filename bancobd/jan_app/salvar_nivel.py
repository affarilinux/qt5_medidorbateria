'''
    CONFIGURACOES app
'''
from configuracoesapp.numerostrig import NUMS1,NUMS2,NUMS3
from configuracoesapp.string_letra import JANELA2,JANELA3,JANELA5


class NivelJanela3:

    def spin_jan2_frameproc(self,spi):
        
        self.ativar_banco1()

        self.cur.execute("SELECT   NIVEL_JANELA  from JANELA3 WHERE ID_JANELA = ?",(spi,))
        spin_ler_3 = self.cur.fetchone()

        for row_sp1  in spin_ler_3:
                
                self.spin.setValue(row_sp1)

        self.sair_banco1()
            
           
    def quantidade_banco_jan3(self,value_frame5,num_ry):

        self.ativar_banco1()

        self.cur.execute("UPDATE JANELA3 SET NIVEL_JANELA  = ? WHERE ID_JANELA = ?",(value_frame5,num_ry))

        self.commit_banco1()
        self.sair_banco1()
