import time

class SalvarProcessador:

    def processos_processador_salvar(self):

        named_tuple = time.localtime() # get struct_time

        time_string = time.strftime("%Y/%m/%d", named_tuple)
        time_string1 = time.strftime("%H:%M:%S", named_tuple)

        seconds = time.time()
        time_str_seg = int(seconds)
        
        self.ativar_banco()

        self.inserir_data(time_string)
        self.inserir_horas(time_string1)
        self.marcar_segundo_internacional(time_str_seg)

        self.ler_banco_data(time_string,time_string1,time_str_seg)

        self.commit_banco()
        self.sair_banco()

    def ler_banco_data(self,dat,hor,seg):

        self.cursorsq.execute("SELECT ID_DATA from DATA_SISTEMA WHERE data_dia = ?",(dat,))
        record_sel0 = self.cursorsq.fetchone()

        for row_sel0  in record_sel0:
            r_s_0 = row_sel0

        self.cursorsq.execute("SELECT ID_HORAS from HORAS WHERE horas_dia = ?",(hor,))
        record_sel1 = self.cursorsq.fetchone()

        for row_sel1  in record_sel1:
            r_s_1 = row_sel1

        self.cursorsq.execute("SELECT ID_SEGUNDOS from SEGUNDOS WHERE segundos = ?",(seg,))
        record_sel2 = self.cursorsq.fetchone()

        for row_sel2  in record_sel2:
            r_s_2 = row_sel2

        self.banco_processador_insert(row_sel0,row_sel1,row_sel2)


    def banco_processador_insert(self,chave0,chave1,chave2):

        self.cursorsq.execute(
            """INSERT INTO PROCESSADOR(
                numero_dia, data_processador,horas_processador,
                porcentagem_processador ) 
                VALUES (?,?,?,?)""",(
                    chave2,chave0,chave1,self.filtra_calculo_sistema))

