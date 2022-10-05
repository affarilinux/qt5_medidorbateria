import sqlite3
from configuracoesapp.numero import NUM0,NUM1

'''
    configuracoesapp
'''
from configuracoesapp.numerostrig import NUMS1,NUMS2,NUMS3,NUMS0
from configuracoesapp.string_letra import true_s,false_s
from configuracoesapp.letra import  none_lt

class Bancosqlite:

    def __init__(self):
        super().__init__()

        self.ativar_banco()
        self.criar_tabela()
        self.sair_banco()

        self.ativar_banco()
        self.organizacao_tabelas_inicializacao()
        self.commit_banco()
        self.sair_banco()

        self.ativar_banco()
        self.apagar_dados_tb()
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
            data_processador INT,
            horas_processador INT,
            porcentagem_processador FLOAT,
            FOREIGN KEY(numero_dia) REFERENCES SEGUNDOS(ID_SEGUNDOS),
            FOREIGN KEY(data_processador) REFERENCES DATA_SISTEMA(ID_DATA),
            FOREIGN KEY(horas_processador) REFERENCES HORAS(ID_HORAS)
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

                       
    ## -------------------------------------------
    ## apagar dados
    def apagar_dados_tb(self):

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
                            print(self.vb, self.drink)
                            #print("as",self.procv)
                        
                            
                            
                            self.cursorsq.execute("DELETE from PROCESSADOR where numero_dia = ? ", (self.sdfg,))

                            #print(self.procv)

                        self.sdfg = self.sdfg - 1
                        self.procv = dest1

            calculo_operacao(self)

        except TypeError:

            pass

                   



            '''if 

                cal  = f - 1

                loop(self,cal)'''

            '''elif g >= self.drink:

                clac = f -1

                apagar_linha(self,clac)'''




        
        
                #apagar_linha(self,str(s_list),str(segu))

        


               
        ''' ss = str(s_list)

                #print(ss[0])

                gh = ss[0:9]
                print(gh)'''

        '''self.cursorsq.execute("SELECT ID_SEGUNDOS FROM SEGUNDOS where  segundos LIKE '"+gh+"%'")
                recosegs = self.cursorsq.fetchall()
                #print(recosegs)
                #print(len(recosegs))


                for fg in recosegs:
                    print(fg)'''





        '''numbers = []

        self.cursorsq.execute("SELECT numero_dia FROM PROCESSADOR")
        recoR_IDs = self.cursorsq.fetchall()

        for r_id3 in recoR_IDs:
            numbers.append(r_id3)

        max_value = None
        max_idx = None

        for idx, num in enumerate(numbers):
            if (max_value is None or num > max_value):
                max_value = num
                max_idx = idx

        self.if_id_cham = 0
        self.var_status = None
        self.var_lop = None

        def deletar_linhadb(self,vl_mun,bo):
            
            
            self.cursorsq.execute("DELETE from PROCESSADOR where numero_dia = ? ",(vl_mun >= bo,))

            wi = vl_mun
           
            df = vl_mun
            
            while wi >=0:
                gh= numbers[]
                for del_list in gh:
                
                 
                    wi = del_list-1
                    df = del_list -1

                    print(del_list)'''



                

                    #self.cursorsq.execute("SELECT  id_processo from  PROCESSADOR WHERE numero_dia = ?",(del_list,))
                #del_iddb = self.cursorsq.fetchone()

                #for apagar in del_iddb:
                   

            #funcao_de_controle_status_del(self,vl_mun)

        '''def funcao_de_controle_status_del(self,idx):
            print(idx)

            for dell in range(idx,-1,-1):
                pri = numbers[dell]
                for diel in pri:
                    #print(diel)
                    deletar_linhadb(self,diel)

                    #deletar_linhadb(self,)

        def ler_banco_variaveis(self,min):

            ler_lista = numbers[min]
            for mx_list in ler_lista:
            
                self.cursorsq.execute("SELECT  segundos from  SEGUNDOS WHERE ID_SEGUNDOS = ?",(mx_list,))
                rec_dest1 = self.cursorsq.fetchone()

                for dest1 in rec_dest1:

                    if self.if_id_cham == 0:
                        self.var_status = dest1
                        self.if_id_cham = 1
                    #print(dest1)

                    funcao_controle_estatus(self,min,dest1)


        def funcao_controle_estatus(self,procs,segu):

            v_processo = self.var_status - 60*60*24

            if segu >= v_processo:

                pc_tb = procs-1
                ler_banco_variaveis(self,pc_tb)

                else:
                
                pti = numbers[0]
                for biu in pti:
                    print(biu)

                    # deletar_linhadb(self,v_processo,biu)

            for dell in range(pc_tb,-1,-1):
                    pri = numbers[dell]
                    for diel in pri:
                        print(diel)
                        #deletar_linhadb(self,diel)
                #self.var_lop = procs
                #funcao_de_controle_status_del(self,procs)
                #print(procs)
                #deletar_linhadb(self,procs)'''

            


        #ler_banco_variaveis(self,max_idx)

                        
        
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




            
        


    