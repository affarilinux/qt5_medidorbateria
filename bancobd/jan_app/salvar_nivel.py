'''
    CONFIGURACOES app
'''
from configuracoesapp.numerostrig import NUMS1,NUMS2,NUMS3
from configuracoesapp.string_letra import JANELA2,JANELA3,JANELA5


class NivelJanela3:

    def spin_jan2_frameproc(self):
        
        self.ativar_banco1()

        if  self.if_var ==  JANELA2:
            self.cur.execute("SELECT   NIVEL_JANELA  from JANELA3 WHERE ID_JANELA = ?",(NUMS2,))
            spin_ler = self.cur.fetchone()

            for row_sp  in spin_ler:
               
                self.spin.setValue(row_sp)

        elif self.if_var ==  JANELA3:
            self.cur.execute("SELECT   NIVEL_JANELA  from JANELA3 WHERE ID_JANELA = ?",(NUMS3,))
            spin_ler = self.cur.fetchone()

            for row_sp  in spin_ler:
               
                self.spin.setValue(row_sp)

        elif self.if_var ==  JANELA5:
            self.cur.execute("SELECT   NIVEL_JANELA  from JANELA3 WHERE ID_JANELA = ?",(NUMS1,))
            spin_ler = self.cur.fetchone()

            for row_sp  in spin_ler:
               
                self.spin.setValue(row_sp)

        self.sair_banco1()
            
           
    def quantidade_banco_jan3(self,value_frame5,num_ry):

        self.ativar_banco1()

        self.cur.execute("UPDATE JANELA3 SET NIVEL_JANELA  = ? WHERE ID_JANELA = ?",(value_frame5,num_ry))

        self.commit_banco1()
        self.sair_banco1()
