import time 

'''
    CONFIGURACOES APP
'''

from configuracoesapp.letra import none_lt

class DataAtual:

    def inserir_data(self,str_data):

        self.cursorsq.execute("SELECT * from DATA_SISTEMA WHERE data_dia = ?",(str_data,))
        record_dia = self.cursorsq.fetchone()

        if record_dia == none_lt:
            
            self.cursorsq.execute("INSERT INTO DATA_SISTEMA(data_dia) VALUES (?)",(str_data,))

    def inserir_horas(self,str_hora):
    
        self.cursorsq.execute("SELECT * from HORAS WHERE horas_dia = ?",(str_hora,))
        record_horas = self.cursorsq.fetchone()

        if record_horas == none_lt:
            
            self.cursorsq.execute("INSERT INTO HORAS(horas_dia) VALUES (?)",(str_hora,))

    def marcar_segundo_internacional(self,segundo_atual):

        self.cursorsq.execute("SELECT * from  SEGUNDOS WHERE segundos = ?",(segundo_atual,))
        record_seg = self.cursorsq.fetchone()

        if record_seg == none_lt:
            
            self.cursorsq.execute("INSERT INTO  SEGUNDOS(segundos) VALUES (?)",(segundo_atual,))
