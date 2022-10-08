import sqlite3
from configuracoesapp.numero import NUM0,NUM1

'''
    configuracoesapp
'''
from configuracoesapp.numerostrig import NUMS1,NUMS2,NUMS3,NUMS4
from configuracoesapp.string_letra import true_s,false_s
from configuracoesapp.letra import  none_lt

class Bancosqlite:

    def __init__(self):
        super().__init__()
        ##----------------------------------------
        self.ativar_banco()

        self.criar_tabela()

        self.sair_banco()
        ##----------------------------------------
        self.ativar_banco()

        self.organizacao_tabelas_inicializacao()

        self.commit_banco()
        self.sair_banco()
        ##----------------------------------------
        self.ativar_banco()

        self.apagar_dados_tb()
        self.apagar_dados_temp()
        self.apagar_dados_ram()

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
        '''
            SISTEMA
        '''
        self.cursorsq.execute(
            """ CREATE TABLE if not exists COOLER(
            id INTEGER PRIMARY KEY,
            estado_cooler text
            )""")

        self.cursorsq.execute(
            """ CREATE TABLE if not exists PROCESSOS_SISTEMA(
            id_processo INTEGER PRIMARY KEY,
            fechar_janela text
            )""")

        '''
            grafico 3
        '''
        self.cursorsq.execute(
            """ CREATE TABLE if not exists JANELA3(
            ID_JANELA INTEGER PRIMARY KEY,
            NIVEL_JANELA INT,
            tipo_chamada TEXT,
            qtd_valor int
            )""")

        '''
            DATA,HORA
        '''
        self.cursorsq.execute(
            """CREATE TABLE if not exists DATA_SISTEMA(
            ID_DATA INTEGER PRIMARY KEY AUTOINCREMENT,
            data_dia DATE
            )""")

        self.cursorsq.execute(
            """CREATE TABLE if not exists HORAS(
            ID_HORAS INTEGER PRIMARY KEY AUTOINCREMENT,
            horas_dia DATETIME UNIQUE
            )""")

        self.cursorsq.execute(
            """CREATE TABLE if not exists SEGUNDOS(
            ID_SEGUNDOS INTEGER PRIMARY KEY AUTOINCREMENT,
            segundos INT
            )""")

        '''
             ESTRUTURA SISTEMA
        '''
        self.cursorsq.execute(
            """ CREATE TABLE if not exists PROCESSADOR(
            id_processo INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_dia INT,
            horas_processador INT,
            porcentagem_processador FLOAT,
            FOREIGN KEY(numero_dia) REFERENCES SEGUNDOS(ID_SEGUNDOS),
            FOREIGN KEY(horas_processador) REFERENCES HORAS(ID_HORAS)
            )""")

        self.cursorsq.execute(
            """ CREATE TABLE if not exists  TEMPERATURADB(
            ID_temperatura INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_dia_temp INT,
            horas_processador_temp INT,
            porcentagem_processador_temp FLOAT,
            FOREIGN KEY(numero_dia_temp) REFERENCES SEGUNDOS(ID_SEGUNDOS),
            FOREIGN KEY(horas_processador_temp) REFERENCES HORAS(ID_HORAS)
            )""")

        self.cursorsq.execute(
            """ CREATE TABLE if not exists  RAMDB(
            ID_temperatura_ram INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_dia_temp_ram INT,
            horas_processador_temp_ram INT,
            porcentagem_processador_temp_ram FLOAT,
            FOREIGN KEY(numero_dia_temp_ram) REFERENCES SEGUNDOS(ID_SEGUNDOS),
            FOREIGN KEY(horas_processador_temp_ram) REFERENCES HORAS(ID_HORAS)
            )""")

        self.cursorsq.execute(
            """ CREATE TABLE if not exists  BATERA_GRAFO(
            ID_temperatura_BAT INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_dia_temp_BAT INT,
            horas_processador_temp_BAT INT,
            porcentagem_processador_temp_BAT FLOAT,
            FOREIGN KEY(numero_dia_temp_BAT) REFERENCES SEGUNDOS(ID_SEGUNDOS),
            FOREIGN KEY(horas_processador_temp_BAT) REFERENCES HORAS(ID_HORAS)
            )""")
    ##
    
    def organizacao_tabelas_inicializacao(self):

        ##----------------------------------------
        ## processo sistema

        self.cursorsq.execute("SELECT * from PROCESSOS_SISTEMA WHERE id_processo = ?",(NUMS1,))
        record_1 = self.cursorsq.fetchone()
        
        if record_1 == none_lt:
            
            self.cursorsq.execute("INSERT INTO PROCESSOS_SISTEMA(id_processo,fechar_janela) VALUES (?,?)",(NUMS1,false_s))
            ##"INSERT INTO COOLER VALUES ('"++",'"++"')""

        elif record_1 != none_lt:
            
            self.cursorsq.execute("UPDATE PROCESSOS_SISTEMA SET fechar_janela = ?",(false_s,))
        
        ##----------------------------------------
        ## janela3
        ##  processador
        self.cursorsq.execute("SELECT * from JANELA3 WHERE ID_JANELA = ?",(NUMS1,))
        record_niv = self.cursorsq.fetchone()
        
        if record_niv == none_lt:
            
            self.cursorsq.execute(
                """INSERT INTO JANELA3(
                    ID_JANELA,NIVEL_JANELA,tipo_chamada ) 
                    VALUES (?,?,?)""",(NUMS1,100,false_s))

        elif record_niv != none_lt:

             self.cursorsq.execute("UPDATE  JANELA3 SET tipo_chamada = ?where ID_JANELA = ?",(false_s,1))

        ## ram
        self.cursorsq.execute("SELECT * from JANELA3 WHERE ID_JANELA = ?",(NUMS2,))
        record_niv2 = self.cursorsq.fetchone()
        
        if record_niv2 == none_lt:
            
            self.cursorsq.execute(
                """INSERT INTO JANELA3(
                    ID_JANELA,NIVEL_JANELA,tipo_chamada ) 
                    VALUES (?,?,?)""",(NUMS2,100,false_s))

        elif record_niv2 != none_lt:

             self.cursorsq.execute("UPDATE  JANELA3 SET tipo_chamada = ?where ID_JANELA = ?",(false_s,2))

        ## temperatura
        self.cursorsq.execute("SELECT * from JANELA3 WHERE ID_JANELA = ?",(NUMS3,))
        record_niv2 = self.cursorsq.fetchone()
        
        if record_niv2 == none_lt:
            
            self.cursorsq.execute(
                """INSERT INTO JANELA3(
                    ID_JANELA,NIVEL_JANELA,tipo_chamada,qtd_valor ) 
                    VALUES (?,?,?,?)""",(NUMS3,100,false_s,0))

        elif record_niv2 != none_lt:

             self.cursorsq.execute("UPDATE  JANELA3 SET tipo_chamada = ?,qtd_valor = ?  where ID_JANELA = ?",(false_s,0,3))

        ## temperatura
        self.cursorsq.execute("SELECT * from JANELA3 WHERE ID_JANELA = ?",(NUMS4,))
        record_niv4 = self.cursorsq.fetchone()
        
        if record_niv4 == none_lt:
            
            self.cursorsq.execute(
                """INSERT INTO JANELA3(
                    ID_JANELA,NIVEL_JANELA,tipo_chamada,qtd_valor ) 
                    VALUES (?,?,?,?)""",(NUMS4,99,false_s,100))

        elif record_niv2 != none_lt:

             self.cursorsq.execute("UPDATE  JANELA3 SET tipo_chamada = ?  where ID_JANELA = ?",(false_s,4))

                       
    ## -------------------------------------------
    ## apagar dados
    ## janela5
    def apagar_dados_tb(self):

        ## inicio processo None()-try
        try:
            self.vb = None
            self.drink = None
            self.sdfg = None
            self.procv = None

            self.cursorsq.execute("SELECT MAX(numero_dia) FROM PROCESSADOR")
            recoR_IDs = self.cursorsq.fetchone()

            for sdf in recoR_IDs:

                self.sdfg = sdf
                
                self.cursorsq.execute("SELECT segundos FROM SEGUNDOS where ID_SEGUNDOS = ?", (sdf,))
                recoseg = self.cursorsq.fetchone()

                for segu in recoseg:

                
                    self.procv = segu

                    self.vb = segu - 60*60*24


            self.cursorsq.execute("SELECT MIN(numero_dia) FROM PROCESSADOR")
            recoR_I = self.cursorsq.fetchone()

            for sdf_ in recoR_I:

                self.cursorsq.execute("SELECT segundos FROM SEGUNDOS where ID_SEGUNDOS = ?", (sdf_,))
                recoseg_ = self.cursorsq.fetchone()

                for segu_ in recoseg_:

                    self.drink = segu_
                    

            def calculo_operacao(self):
               
                
                while self.procv >= self.drink:

                    self.cursorsq.execute("SELECT  segundos from  SEGUNDOS WHERE ID_SEGUNDOS = ?",(self.sdfg,))
                    rec_dest1 = self.cursorsq.fetchone()

                    for dest1 in rec_dest1:

                        if self.procv < self.vb and self.procv >= self.drink:
                        
                            self.cursorsq.execute("DELETE from PROCESSADOR where numero_dia = ? ", (self.sdfg,))

                        self.sdfg = self.sdfg - 1
                        self.procv = dest1

            calculo_operacao(self)

        except TypeError:

            pass
    ## janela3
    def apagar_dados_temp(self):
    
        ## inicio processo None()-try
        try:
            self.vb_t3 = None
            self.drink_t3 = None
            self.sdfg_t3 = None
            self.procv_t3 = None

            self.cursorsq.execute("SELECT MAX(numero_dia) FROM PROCESSADOR")
            recoR_IDs_t3 = self.cursorsq.fetchone()

            for sdf_t3 in recoR_IDs_t3:

                self.sdfg_t3 = sdf_t3
                
                self.cursorsq.execute("SELECT segundos FROM SEGUNDOS where ID_SEGUNDOS = ?", (sdf_t3,))
                recoseg_t3 = self.cursorsq.fetchone()

                for segu_t3 in recoseg_t3:

                
                    self.procv_t3 = segu_t3

                    self.vb_t3 = segu_t3 - 60*60*24


            self.cursorsq.execute("SELECT MIN(numero_dia) FROM PROCESSADOR")
            recoR_I_tt3 = self.cursorsq.fetchone()

            for sdf_tt3 in recoR_I_tt3:

                self.cursorsq.execute("SELECT segundos FROM SEGUNDOS where ID_SEGUNDOS = ?", (sdf_tt3,))
                recoseg_tt23 = self.cursorsq.fetchone()

                for segu_tt23 in recoseg_tt23:

                    self.drink_t3 = segu_tt23
                    

            def calculo_operacao_3(self):
               
                
                while self.procv_t3 >= self.drink_t3:

                    self.cursorsq.execute("SELECT  segundos from  SEGUNDOS WHERE ID_SEGUNDOS = ?",(self.sdfg_t3,))
                    rec_dest1_tt33 = self.cursorsq.fetchone()

                    for dest1_tt33 in rec_dest1_tt33:

                        if self.procv_t3 < self.vb_t3 and self.procv_t3 >= self.drink_t3:
                        
                            self.cursorsq.execute("DELETE from PROCESSADOR where numero_dia = ? ", (self.sdfg_t3,))

                        self.sdfg_t3 = self.sdfg_t3 - 1
                        self.procv_t3 = dest1_tt33

            calculo_operacao_3(self)

        except TypeError:

            pass

    ## janela2
    def apagar_dados_ram(self):
    
        ## inicio processo None()-try
        try:
            self.vb_t2 = None
            self.drink_t2 = None
            self.sdfg_t2 = None
            self.procv_t2 = None

            self.cursorsq.execute("SELECT MAX(numero_dia) FROM PROCESSADOR")
            leia_t2 = self.cursorsq.fetchone()

            for rlop_t2 in leia_t2:

                self.sdfg_t2 = rlop_t2
                
                self.cursorsq.execute("SELECT segundos FROM SEGUNDOS where ID_SEGUNDOS = ?", (rlop_t2,))
                leiat_t2 = self.cursorsq.fetchone()

                for Rlop_segur_t2 in leiat_t2:

                
                    self.procv_t2 = Rlop_segur_t2

                    self.vb_t2 = Rlop_segur_t2 - 60*60*24


            self.cursorsq.execute("SELECT MIN(numero_dia) FROM PROCESSADOR")
            leiamim_dia_t2 = self.cursorsq.fetchone()

            for rlop_mim_dia_t2 in leiamim_dia_t2:

                self.cursorsq.execute("SELECT segundos FROM SEGUNDOS where ID_SEGUNDOS = ?", (rlop_mim_dia_t2,))
                leia_mdia_tt23 = self.cursorsq.fetchone()

                for for_dia_mim_t2 in leia_mdia_tt23:

                    self.drink_t2 = for_dia_mim_t2
                    

            def calculo_operacao_2(self):
               
                
                while self.procv_t2 >= self.drink_t2:

                    self.cursorsq.execute("SELECT  segundos from  SEGUNDOS WHERE ID_SEGUNDOS = ?",(self.sdfg_t2,))
                    leia_leia_t2 = self.cursorsq.fetchone()

                    for fim_proc_dest in leia_leia_t2:

                        if self.procv_t2 < self.vb_t2 and self.procv_t2 >= self.drink_t2:
                        
                            self.cursorsq.execute("DELETE from PROCESSADOR where numero_dia = ? ", (self.sdfg_t2,))

                        self.sdfg_t2 = self.sdfg_t2 - 1
                        self.procv_t2 = fim_proc_dest

            calculo_operacao_2(self)

        except TypeError:

            pass
    
    
    ##--------------------------------------------
    # close da janela
    def atualizar_processo_sistema(self):

        self.ativar_banco()

        self.cursorsq.execute("SELECT fechar_janela FROM PROCESSOS_SISTEMA")
        record_2 = self.cursorsq.fetchone()

        for row_at  in record_2:

            if row_at == false_s:
                self.cursorsq.execute("UPDATE PROCESSOS_SISTEMA SET fechar_janela = ?",(true_s,))

        self.commit_banco()
        self.sair_banco()




            
        


    