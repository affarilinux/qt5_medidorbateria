'''
    configuracoes app
'''
from configuracoesapp.string_letra import BATERIA_S
class BateriaJan1:

    def avisar_salvar_jan3(self,batera):

        self.ativar_banco()

        self.cursorsq.execute(
                "SELECT  NIVEL_JANELA,qtd_valor FROM JANELA3 where ID_JANELA = ?",(4,))

        n2j3_4 = self.cursorsq.fetchone()
               
        if batera <= n2j3_4[0] or batera >= n2j3_4[1]:
            
            self.cursorsq.execute(
            "UPDATE  JANELA3 SET tipo_chamada=?  where ID_JANELA = ?",(BATERIA_S,4))

            self.ativar_janela_temporaria()

        self.commit_banco()
        self.sair_banco()