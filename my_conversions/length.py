class Length:
    def __init__(self, length):
        self.length = length

    def cm_to_m(self):   
        return self.length/100 
    
    def cm_to_km(self):
        return self.length/100000 
    
    def m_to_cm(self):
        return self.length * 100
    
    def m_to_km(self):
        return self.length/1000

    def km_to_cm(self):
        return self.length * 100000
          
