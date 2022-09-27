'''
    CONFIGURACOES app
'''
from configuracoesapp.numerostrig import NUMS1
from configuracoesapp.letra import none_lt

class NivelJanela3:

    def quantidade_banco_jan3(self,value_frame5):

        self.ativar_banco1()

        self.cur.execute("SELECT * from JANELA3 WHERE ID_JANELA = ?",(NUMS1,))
        record_niv = self.cur.fetchone()
        if record_niv == none_lt:
            
            self.cur.execute("INSERT INTO JANELA3(ID_JANELA,NIVEL_JANELA ) VALUES (?,?)",(NUMS1,value_frame5))
            
        elif record_niv != none_lt:
            
            self.cur.execute("UPDATE JANELA3 SET NIVEL_JANELA  = ?",(value_frame5,))

        self.commit_banco1()
        self.sair_banco1()
