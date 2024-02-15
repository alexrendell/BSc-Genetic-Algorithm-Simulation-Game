from resources import Resources
import Thesis2.buildings as buildings


class Village:
    def __init__(self, name, resources, population):
        self.name = name
        self.population = population
        self.resources = resources
        self.owned_buildings = []
        self.turn = 0
        #self.res = Resources(self)
        #self.att = Attacking(self)
        #self.defe = Defensive(self)
        #self.harv = Harvesting(self)
        #self.res.add_wood(100)
        #self.att.buy_tank()
        #total_resouces = self.res.get_coal
        #algorithm.fitness(self,name, total_resouces)
        #algorithm.fitness(name,self.res.get_wood,self.res.get_coal,
                          #self.res.get_metal,self.res.get_gold)
        
    #Purchasing a building
    def buy_building(self, building_number):
        #Check if village has enough resources
        building = buildings.all_buildings[building_number]
        if self.resources >= building.cost:
            #Deduct cost from village resources
            self.resources -= building.cost
            #Add building to list of harvesting buldings
            self.owned_buildings.append(building)
            print(f"{self.name} purchased {building.name}")
        else:
            print(f"{self.name} has insufficient resources to buy {building.name}")

    def fire_power(self):
        return self.att.all_units()
    
    def all_materials(self):
        return self.res.all_resources()