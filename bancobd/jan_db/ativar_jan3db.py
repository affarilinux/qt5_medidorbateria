
'''
    CONFIGURACOES APP
'''
from configuracoesapp.numerostrig import NUMS1,NUMS2,NUMS3
from configuracoesapp.string_letra import PROCESSADOR,RAM_S
class AtivarJanela3:

    def ativar_janela_processador(self,num_proc):

        self.ativar_banco()

        self.cursorsq.execute("SELECT NIVEL_JANELA from JANELA3 WHERE ID_JANELA = ?",(NUMS1,))
        jan_proc3 = self.cursorsq.fetchone()

        for row_at3 in jan_proc3:
        
            if num_proc >= row_at3:

                self.ativar_janela_temporaria()

                self.cursorsq.execute("UPDATE JANELA3 SET tipo_chamada = ? WHERE ID_JANELA = ?",(PROCESSADOR,NUMS1))
                
        self.commit_banco()
        self.sair_banco()


    def ativar_janela_ram(self,num_ram):
    
        self.ativar_banco()

        self.cursorsq.execute("SELECT NIVEL_JANELA from JANELA3 WHERE ID_JANELA = ?",(NUMS2,))
        jan_proc3_2 = self.cursorsq.fetchone()

        for row_at3_2 in jan_proc3_2:            
        
            if num_ram >= row_at3_2:

                self.ativar_janela_temporaria()

                self.cursorsq.execute("UPDATE JANELA3 SET tipo_chamada = ? WHERE ID_JANELA = ?",(RAM_S,NUMS2))
                
        self.commit_banco()
        self.sair_banco()

    def ativar_janela_temperatura(self,processor,core,core1,core2,wifi):
        
        self.ativar_banco()

        self.cursorsq.execute("SELECT NIVEL_JANELA from JANELA3 WHERE ID_JANELA = ?",(NUMS3,))
        jan_proc3_3 = self.cursorsq.fetchone()

        for row_at3_3 in jan_proc3_3:            
        
            if processor >= row_at3_3:

                self.ativar_janela_temporaria()

                self.cursorsq.execute(
                    "UPDATE JANELA3 SET tipo_chamada = ?,qtd_valor = ? WHERE ID_JANELA = ?",("FREQUÊNCIA",processor,NUMS3))

            elif core >= row_at3_3:
    
                self.ativar_janela_temporaria()

                self.cursorsq.execute(
                    "UPDATE JANELA3 SET tipo_chamada = ?,qtd_valor = ? WHERE ID_JANELA = ?",("CORE",core,NUMS3))
            
            elif core1 >= row_at3_3:
        
                self.ativar_janela_temporaria()

                self.cursorsq.execute(
                    "UPDATE JANELA3 SET tipo_chamada = ?,qtd_valor = ? WHERE ID_JANELA = ?",("CORE1",core1,NUMS3))
            
            elif core2 >= row_at3_3:
        
                self.ativar_janela_temporaria()

                self.cursorsq.execute(
                    "UPDATE JANELA3 SET tipo_chamada = ?,qtd_valor = ? WHERE ID_JANELA = ?",("CORE2",core2,NUMS3))
            
            elif wifi >= row_at3_3:
        
                self.ativar_janela_temporaria()

                self.cursorsq.execute(
                    "UPDATE JANELA3 SET tipo_chamada = ?,qtd_valor = ? WHERE ID_JANELA = ?",("WIFI",wifi,NUMS3))

                
        self.commit_banco()
        self.sair_banco()