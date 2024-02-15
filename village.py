from harvesting_items import Harvesting
from attacking_items import Attacking
from defensive_items import Defensive
from resources import Resources
import algorithm


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
        total_resouces = self.res.get_coal
        algorithm.fitness(self,name, total_resouces)
        #algorithm.fitness(name,self.res.get_wood,self.res.get_coal,
                          #self.res.get_metal,self.res.get_gold)
        

    def fire_power(self):
        return self.att.all_units()
    
    def all_materials(self):
        return self.res.all_resources()