from PyQt5.QtWidgets import QMainWindow
from PyQt5 import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

'''
    CONFIGURACOES APP
'''
from configuracoesapp.string_letra import PROCESSADOR

class JanelaGrafico (QMainWindow):

   
    def umb(self):

        self.canvas = FigureCanvas(plt.Figure(figsize=(15, 6),dpi=80))

        self.chart = self.canvas
        
        self.chart.setWindowTitle("HARDWARE")
        self.chart.move(600,600)
        self.chart.resize(800,400)
           
        self.ucv()
        
        self.chart.show()

                           
    def ucv(self):
            self.ax = self.canvas.figure.subplots()
            
            
            #self.mostrar_grafico_ax()
            self.mostrar_grafico_if()
                       
            self.ax.grid()

            
            
            

            

    
        