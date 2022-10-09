
import matplotlib.ticker as ticker
'''
    configuracoes app
'''
from  configuracoesapp.string_letra import JANELA1,JANELA2,JANELA3,JANELA5,PROCESSADOR
class MostrarGrafico:
       
    def mostrar_grafico_if(self):
       

        if self.if_var == JANELA1:

            if self.entre_2 ==1:
                #self.mostrar_grafico_1_1()
                print(1)

            elif self.entre_2 == 2:
                
                print(2)

        elif self.if_var == JANELA2:
            
            self.mostrar_grafico_ax_2()

        elif self.if_var == JANELA3:
            
            self.mostrar_grafico_ax_3()

        elif self.if_var == JANELA5:

            self.mostrar_grafico_ax_5()

    ##--------------------------------------------
    ## grafico 1
    ## parte 1
    def mostrar_grafico_1_1(self):
        print("parte1")

    def mostrar_grafico_1_2(self):
        print("parte2")

    ##--------------------------------------------
    ##graficop 3
    def mostrar_grafico_ax_2(self):

        self.ax.set(xlabel='tempo', ylabel='QUANTIDADE',
               title="RAM")

        self.lista_1_grafico_2 = []
        self.lista_2_grafico_2 = []

        self.ativar_banco1()#**

        def select_data_db(self,list_hor_2): #funcao
    
            
            self.cur.execute("SELECT  horas_dia  from HORAS WHERE ID_HORAS = ?",(list_hor_2,))
            record_sel_2 = self.cur.fetchone()

            for row_se2  in record_sel_2:
                self.lista_1_grafico_2.append(str(row_se2))

        ## eixo xxx
        self.cur.execute(
            """SELECT horas_processador_temp_ram
            from RAMDB""")
        grafo_append_horas2 = self.cur.fetchall()
        
        for isso12 in grafo_append_horas2:
            select_data_db(self,isso12[0])

         ### eixo y
        self.cur.execute(
            """SELECT porcentagem_processador_temp_ram 
            from RAMDB""")
        graf_numero_linhas2 = self.cur.fetchall()

        for row_y2 in graf_numero_linhas2:

            self.lista_2_grafico_2.append(row_y2[0])
        
        self.sair_banco1()#**
        
        x2 = self.lista_1_grafico_2
        y2 = self.lista_2_grafico_2

        self.ax.plot(x2,y2)

        ass_2 = len(self.lista_1_grafico_2)
        print("ram",ass_2)

        self.len_ass(ass_2)


    ##--------------------------------------------
    ##graficop 3
    def mostrar_grafico_ax_3(self):

        self.ax.set(xlabel='tempo', ylabel='TEMPERATURA',
               title="TEMPERATURA")

        self.lista_1_grafico = []
        self.lista_2_grafico = []

        self.ativar_banco1()#**

        def select_data_db(self,list_hor_3): #funcao
    
            
            self.cur.execute("SELECT  horas_dia  from HORAS WHERE ID_HORAS = ?",(list_hor_3,))
            record_sel_3 = self.cur.fetchone()

            for row_se3  in record_sel_3:
                self.lista_1_grafico.append(str(row_se3))

        ## eixo xxx
        self.cur.execute(
            """SELECT horas_processador_temp
            from TEMPERATURADB""")
        grafo_append_horas3 = self.cur.fetchall()
        
        for isso13 in grafo_append_horas3:
            select_data_db(self,isso13[0])

         ### eixo y
        self.cur.execute(
            """SELECT porcentagem_processador_temp 
            from TEMPERATURADB""")
        graf_numero_linhas3 = self.cur.fetchall()

        for row_y3 in graf_numero_linhas3:

            self.lista_2_grafico.append(row_y3[0])
        
        self.sair_banco1()#**
        
        x3 = self.lista_1_grafico
        y3 = self.lista_2_grafico

        self.ax.plot(x3,y3)

        ass_3 = len(self.lista_1_grafico)
        print("temperatura",ass_3)

        self.len_ass(ass_3)


    ##--------------------------------------------
    ##graficop 5
    def mostrar_grafico_ax_5(self):

        self.ax.set(xlabel='tempo', ylabel='frequência',
               title=PROCESSADOR)

        self.str_list_hor = []
        self.str_list_porc = []

        self.ativar_banco1()#**

        def select_data_db(self,list_hor): #funcao
    
            
            self.cur.execute("SELECT  horas_dia  from HORAS WHERE ID_HORAS = ?",(list_hor,))
            record_sel_ = self.cur.fetchone()

            for row_se  in record_sel_:
                self.str_list_hor.append(str(row_se))

        ## eixo xxx
        self.cur.execute(
            """SELECT horas_processador
            from PROCESSADOR""")
        graf_numero_linhas_1 = self.cur.fetchall()
        
        for isso1 in graf_numero_linhas_1:
            select_data_db(self,isso1[0])

         ### eixo y
        self.cur.execute(
            """SELECT porcentagem_processador 
            from PROCESSADOR""")
        graf_numero_linhas = self.cur.fetchall()

        for row_y in graf_numero_linhas:

            self.str_list_porc.append(row_y[0])
        
        self.sair_banco1()#**
        
        x = self.str_list_hor
        y = self.str_list_porc

        self.ax.plot(x,y)

        ass = len(self.str_list_hor)
        print("processador",ass)

        self.len_ass(ass)

    ##--------------------------------------------
    ##

    def len_ass(self,ass):

        def plot_5(self,ticker_s):##funmcao

            self.ax.xaxis.set_major_locator(ticker.MultipleLocator(ticker_s))
            
        if ass < 100:

            plot_5(self,4)

        elif ass < 500:

            plot_5(self,20)

        elif ass < 1000:

            plot_5(self,34)

        elif ass < 2000:

            plot_5(self,50)

        elif ass < 5000:

            plot_5(self,80)

        elif ass < 10000:
    
            plot_5(self,100)

        elif ass < 20000:
        
            plot_5(self,142)

        elif ass < 40000:
            
            plot_5(self,200)

        elif ass < 60000:
            
            plot_5(self,250)

        elif ass <= 84400:
            
            plot_5(self,211)
        
        elif ass > 84400:
            
            plot_5(self,500)




        
       
        
        
       
           
       
        
    
    
        
       

            

                