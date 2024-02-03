class Attacking:
    def __init__(self, Village):
        self.tank = 0
    
    def buy_tank(self):
        self.tank +=1
        
    def all_units(self):
        return f"Tank: {self.tank}"