import time

class SalvarProcessador:

    def funcao_time_salvar_db(self):

        self.ativar_banco()

        named_tuple = time.localtime() # get struct_time

        #time_string = time.strftime("%Y/%m/%d", named_tuple)
        time_string1 = time.strftime("%H:%M:%S", named_tuple)

        seconds = time.time()
        time_str_seg = int(seconds)

        #self.inserir_data(time_string)
        self.inserir_horas(time_string1)
        self.marcar_segundo_internacional(time_str_seg)

        '''self.cursorsq.execute("SELECT ID_DATA from DATA_SISTEMA WHERE data_dia = ?",(dat,))
        record_sel0 = self.cursorsq.fetchone()

        for row_sel0  in record_sel0:
            r_s_0 = row_sel0'''

        self.cursorsq.execute("SELECT ID_HORAS from HORAS WHERE horas_dia = ?",(time_string1,))
        self.record_sel1 = self.cursorsq.fetchone()
       
        self.cursorsq.execute("SELECT ID_SEGUNDOS from SEGUNDOS WHERE segundos = ?",(time_str_seg,))
        self.record_sel2 = self.cursorsq.fetchone()

        self.commit_banco()
        self.sair_banco()


    ##--------------------------------------------
    def processos_salvar_grafico(self):

        self.funcao_time_salvar_db()
        
        self.ativar_banco()

        ## processador
        self.cursorsq.execute(
            """INSERT INTO PROCESSADOR(
                numero_dia,horas_processador,
                porcentagem_processador ) 
                VALUES (?,?,?)""",(
                    self.record_sel2[0],self.record_sel1[0],self.filtra_calculo_sistema))

        ## temperatura
        self.cursorsq.execute(
            """INSERT INTO TEMPERATURADB(
                numero_dia_temp,horas_processador_temp,
                porcentagem_processador_temp ) 
                VALUES (?,?,?)""",(
                    self.record_sel2[0],self.record_sel1[0],self.calculosoma))

        ## ram
        self.cursorsq.execute(
            """INSERT INTO RAMDB(
                numero_dia_temp_ram,horas_processador_temp_ram,
                porcentagem_processador_temp_ram ) 
                VALUES (?,?,?)""",(
                    self.record_sel2[0],self.record_sel1[0],self.calculo_filtro_informacao))

        self.commit_banco()
        self.sair_banco()

   

    