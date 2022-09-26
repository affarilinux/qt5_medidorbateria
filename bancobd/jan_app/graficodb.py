
import matplotlib.ticker as ticker

class MostrarGrafico:
       
    '''def __init__(self):
        super().__init__()'''

    def mostrar_grafico_ax(self):

        self.str_list_hor = []
        self.str_list_porc = []

        self.ativar_banco1()

        def select_data_db(self,list_hor):
    
            
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
        
        self.sair_banco1()
        
        x = self.str_list_hor
        y = self.str_list_porc

        self.ax.plot(x,y)

        ass = len(self.str_list_hor)
        print(ass)

        def plot_5(self,ticker_s):

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




        
       
        
        
       
           
       
        
    
    
        
       

            

                