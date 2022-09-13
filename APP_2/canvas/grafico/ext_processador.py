from cProfile import label
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class Canvas(FigureCanvas):
    
    def __init__(self,parent):
        fig, self.ax = plt.subplots(figsize=(10, 10), dpi=100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        #t = np.arange(0.1, 2.0, 0.01)
        #s = 1 + np.sin(2 * np.pi * t)
        
        t = [1,2,3,4,5,6]
        s = [0.1,0.2,0.2,0.3,0.2,0.8]
        self.ax.plot(t, s)

        self.ax.set(xlabel='tempo', ylabel='frequência',
               title='PROCESSADOR')
        self.ax.grid()