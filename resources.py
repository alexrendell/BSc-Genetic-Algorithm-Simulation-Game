
class Resources:
    
    # When a village is first created all resources are set to 0
    def __init__(self, Village):
        self.wood = 0
        self.coal = 0
        self.metal = 0
        self.gold = 0
    
    def add_wood(self, amount):
        self.wood += amount
    
    def add_coal(self, amount):
        self.coal += amount
        
    def add_metal(self, amount):
        self.metal += amount
        
    def add_gold(self, amount):
        self.gold += amount
        
    def all_resources(self):
        return f"Wood: {self.wood} Coal: {self.coal} Metal: {self.metal} Gold: {self.gold}"