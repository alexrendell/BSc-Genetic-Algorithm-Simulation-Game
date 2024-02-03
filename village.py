from harvesting_items import Harvesting
from attacking_items import Attacking
from defensive_items import Defensive
from resources import Resources


class Village:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.res = Resources(self)
        self.att = Attacking(self)
        #self.defe = Defensive(self)
        #self.harv = Harvesting(self)
        self.res.add_wood(100)
        self.att.buy_tank()
        

    def fire_power(self):
        return self.att.all_units()
    
    def all_materials(self):
        return self.res.all_resources()