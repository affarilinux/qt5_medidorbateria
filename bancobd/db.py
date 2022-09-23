import sqlite3

'''
    configuracoesapp
'''
from configuracoesapp.numerostrig import NUMS1
from configuracoesapp.string_letra import true_s,false_s
from configuracoesapp.letra import  nome_lt

class Bancosqlite:

    def __init__(self):
        super().__init__()

        self.ativar_banco()
        self.criar_tabela()
        self.organizacao_tabelas_inicializacao()
        self.commit_banco()
        self.sair_banco()
        
    ##
    def ativar_banco(self):
        self.bancovar = sqlite3.connect('bancobd/banco_hard.db')

        self.cursorsq = self.bancovar.cursor()

    def sair_banco(self):
        self.cursorsq.close()
        self.bancovar.close()

    def commit_banco(self):
        self.bancovar.commit()
    ##
    def criar_tabela(self):
        self.cursorsq.execute(""" CREATE TABLE if not exists COOLER(
            id INTEGER PRIMARY KEY,
            estado_cooler text)""")

        self.cursorsq.execute(""" CREATE TABLE if not exists PROCESSOS_SISTEMA(
            id_processo INTEGER PRIMARY KEY,
            fechar_janela text)""")
    ##
    
    def organizacao_tabelas_inicializacao(self):

        self.cursorsq.execute("SELECT * from PROCESSOS_SISTEMA WHERE id_processo = ?",(NUMS1,))
        record_1 = self.cursorsq.fetchone()
        
        if record_1 == nome_lt:
            
            self.cursorsq.execute("INSERT INTO PROCESSOS_SISTEMA(id_processo,fechar_janela) VALUES (?,?)",(NUMS1,false_s))
            ##"INSERT INTO COOLER VALUES ('"++",'"++"')""

        elif record_1 != nome_lt:
            
            self.cursorsq.execute("UPDATE PROCESSOS_SISTEMA SET fechar_janela = ?",(false_s,))

    def atualizar_processo_sistema(self):

        self.ativar_banco()

        self.cursorsq.execute("SELECT fechar_janela FROM PROCESSOS_SISTEMA")
        record_2 = self.cursorsq.fetchone()

        for row_at  in record_2:

            if row_at == false_s:
                self.cursorsq.execute("UPDATE PROCESSOS_SISTEMA SET fechar_janela = ?",(true_s,))

        self.commit_banco()
        self.sair_banco()




            
        


    