
class ApagarTabela:

    def apagar_registro(self):

        self.ativar_banco1()

        self.cur.execute("DELETE from PROCESSADOR ")

        self.cur.execute("DELETE from DATA_SISTEMA ")
        self.cur.execute("DELETE from HORAS ")
        self.cur.execute("DELETE from SEGUNDOS ")
        self.cur.execute("DELETE from sqlite_sequence ")

        

        self.commit_banco1()
        self.sair_banco1()