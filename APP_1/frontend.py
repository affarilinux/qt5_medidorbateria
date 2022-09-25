from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtCore        import QTimer

'''
    CONFIGURACOES APP
'''
from configuracoesapp.numero import ( 
    NUM2,NUM5,NUM10,NUM15,NUM20,NUM25,NUM30,NUM40,
    NUM50,NUM60,NUM70,NUM85,NUM120,NUM125,NUM130,
    NUM140,NUM160,NUM170,NUM175,NUM210,NUM380,NUM5000
    )

class GuiFront(QMainWindow):
    
    def __init__( self ):
    
        super ().__init__() # metodo 
        
        qtimer_front = QTimer        ( self )

        qtimer_front.setInterval     ( NUM5000 )
        qtimer_front.start           ()

        #chamada de funçãO
        qtimer_front.timeout.connect ( self.chamar_front ) 

        ## sistema fixo

        LABEL_MAIN_FIXO = QLabel(self)
        LABEL_MAIN_FIXO.setText("HARDWARE")
        LABEL_MAIN_FIXO.move(NUM50,NUM5)
        LABEL_MAIN_FIXO.resize(NUM130,NUM40)
        LABEL_MAIN_FIXO.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 20px}')# YELLOW

        LABEL_TRACO_FIXO = QLabel(self)
        LABEL_TRACO_FIXO.move(NUM5,NUM40)
        LABEL_TRACO_FIXO.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO.setStyleSheet('QLabel{background-color: #FFFF00;}')
        

        self.BOTAO_APP= QPushButton('aplicativo',self)
        self.BOTAO_APP.move(NUM10,NUM380)#janela
        self.BOTAO_APP.resize(NUM120,NUM40)
        self.BOTAO_APP.setStyleSheet('QPushButton{background-color: #FFFF00; font: bold; font-size: 20px}')#Yellow
        self.BOTAO_APP.clicked.connect(self.ativar_janela)

        self.BOTAO_SAIR = QPushButton('SAIR',self)
        self.BOTAO_SAIR.move(NUM140,NUM380)#janela
        self.BOTAO_SAIR.resize(NUM70,NUM40)
        self.BOTAO_SAIR.setStyleSheet('QPushButton{background-color: #FFFF00; font: italic; font-size: 20px}')# Yellow
        self.BOTAO_SAIR.clicked.connect(self.sair_janela)

        ## BATERIA

        LABEL_BATERIA_FIXO = QLabel(self)
        LABEL_BATERIA_FIXO.setText("BATERIA")
        LABEL_BATERIA_FIXO.move(NUM70,55)
        LABEL_BATERIA_FIXO.resize(NUM175,NUM20)
        LABEL_BATERIA_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 20px}')# Lime

        self.label_100_vav = QLabel(self)
        self.label_100_vav.move(NUM15,NUM85)
        self.label_100_vav.resize(NUM70,NUM25)
        self.label_100_vav.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 18px}')# Lime
        #@
        self.timer_bateria_100()

        self.label_carga = QLabel(self)
        self.label_carga.move(NUM85,NUM85)
        self.label_carga.resize(NUM125,NUM25)
        self.label_carga.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 15px}')# Lime
        #@
        self.timer_bateria_estado()
        ## traços

        LABEL_TRACO_FIXO1 = QLabel(self)
        LABEL_TRACO_FIXO1.move(NUM5,110)
        LABEL_TRACO_FIXO1.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO1.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        LABEL_TRACO_FIXO11 = QLabel(self)
        LABEL_TRACO_FIXO11.move(NUM5,NUM160)
        LABEL_TRACO_FIXO11.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO11.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        LABEL_TRACO_FIXO12 = QLabel(self)
        LABEL_TRACO_FIXO12.move(NUM5,230)
        LABEL_TRACO_FIXO12.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO12.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        LABEL_TRACO_FIXO13 = QLabel(self)
        LABEL_TRACO_FIXO13.move(NUM5,295)
        LABEL_TRACO_FIXO13.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO13.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        LABEL_TRACO_FIXO14 = QLabel(self)
        LABEL_TRACO_FIXO14.move(NUM5,360)
        LABEL_TRACO_FIXO14.resize(NUM210,NUM2)
        LABEL_TRACO_FIXO14.setStyleSheet('QLabel{background-color: #00FF00;}') # Lime

        ## MEMORIA RAM

        LABEL_RAMNOME_FIXO = QLabel(self)
        LABEL_RAMNOME_FIXO.setText("RAM")
        LABEL_RAMNOME_FIXO.move(NUM10,NUM125)
        LABEL_RAMNOME_FIXO.resize(NUM175,25)
        LABEL_RAMNOME_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 25px}')# Lime

        self.label_100_vav_ram = QLabel(self)
        self.label_100_vav_ram.move(90,126)
        self.label_100_vav_ram.resize(NUM130,23)
        self.label_100_vav_ram.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 23px}')# Lime

        self.memoria_ram()

        ## temperatura média

        LABEL_TEMP_FIXO = QLabel(self)
        LABEL_TEMP_FIXO.setText("TEMPERATURA MÉDIA")
        LABEL_TEMP_FIXO.move(NUM15,NUM170)
        LABEL_TEMP_FIXO.resize(185,NUM15)
        LABEL_TEMP_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 15px}')# Lime

        self.label_tempnum = QLabel(self)
        self.label_tempnum.move(NUM60,195)
        self.label_tempnum.resize(NUM130,NUM25)
        self.label_tempnum.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 25px}')# Lime
        self.temperatura_lib()

        ## COOLER

        LABEL_COOLER_FIXO = QLabel(self)
        LABEL_COOLER_FIXO.setText("COOLER")
        LABEL_COOLER_FIXO.move(NUM70,240)
        LABEL_COOLER_FIXO.resize(NUM130,NUM20)
        LABEL_COOLER_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 20px}')# Lime

        self.label_cooler_nome = QLabel(self)
        self.label_cooler_nome.move(NUM40,270)
        self.label_cooler_nome.resize(NUM160,NUM15)
        self.label_cooler_nome.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 15px}')# Lime
        self.leitura_fans()

        ##PROCESSADOR

        LABEL_PROC_FIXO = QLabel(self)
        LABEL_PROC_FIXO.setText("PROCESSADOR")
        LABEL_PROC_FIXO.move(NUM30,305)
        LABEL_PROC_FIXO.resize(NUM170,NUM20)
        LABEL_PROC_FIXO.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 20px}')# Lime

        self.label_100_vav_proc = QLabel(self)
        self.label_100_vav_proc.move(NUM60,330)
        self.label_100_vav_proc.resize(NUM130,NUM25)
        self.label_100_vav_proc.setStyleSheet('QLabel{color: #00FF00;font:bold;font-size: 25px}')# Lime
        self.processador_frequencia()

    def chamar_front(self):

        self.chamada_qtimerbateria()
        self.processador_frequencia ()
        self.memoria_ram()
        self.temperatura_lib()

         ##banco
        self.processos_processador_salvar()

    
       