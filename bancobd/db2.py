import sqlite3

class BancoSqlite3:

    def ativar_banco2(self):
        
        self.bancot22 = sqlite3.connect('bancobd/banco_hard.db')

        self.cursort2 = self.bancot22.cursor()

    
    def commit_banco2(self):
        self.bancot22.commit()

    def sair_banco2(self):
        self.cursort2.close()
        self.bancot22.close()