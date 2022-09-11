import sqlite3

from configuracoesapp.numerostrig import NUMS1

class Bancosqlite:

    def __init__(self):
        super().__init__()

        self.ativar_banco()
        self.criar_tabela()
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
    ##
    def as_cooler(self,cool):
        
        self.cursorsq.execute("SELECT * from COOLER WHERE id = ?",(NUMS1,))
        record = self.cursorsq.fetchone()
        if record == None:
            
            self.cursorsq.execute("INSERT INTO COOLER(id,estado_cooler) VALUES (?,?)",(NUMS1,cool))
            ##"INSERT INTO COOLER VALUES ('"++",'"++"')""

        elif record != None:
            
            self.cursorsq.execute("UPDATE COOLER SET estado_cooler = ?",(cool,))
            
        


    