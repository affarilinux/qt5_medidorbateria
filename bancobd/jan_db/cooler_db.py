'''
    configuracoes app
'''
from configuracoesapp.numerostrig import NUMS1
from configuracoesapp.letra import none_lt

class BancoCooler:

    def as_cooler(self,cool):
        
        self.cursorsq.execute("SELECT * from COOLER WHERE id = ?",(NUMS1,))
        record = self.cursorsq.fetchone()
        if record == none_lt:
            
            self.cursorsq.execute("INSERT INTO COOLER(id,estado_cooler) VALUES (?,?)",(NUMS1,cool))
            ##"INSERT INTO COOLER VALUES ('"++",'"++"')""

        elif record != none_lt:
            
            self.cursorsq.execute("UPDATE COOLER SET estado_cooler = ?",(cool,))