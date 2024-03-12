from resources import Resources
import buildings as buildings


class Village:
    def __init__(self, name, resources, workers):
        self.name = name
        self.workers = workers
        self.resources = resources
        self.owned_buildings = []
        #Add the amount of workers to the list of owned buildings
        for buy_workers in range(workers):
            self.owned_buildings.append(buildings.all_buildings[1])
        self.turn = 0
        
    #Purchasing a building
    def buy_building(self, building_number):
        #Retruns building getting bought
        building = buildings.all_buildings[building_number]
        #Check if village has enough resources
        if self.resources >= building.cost:
            #Deduct cost from village resources
            self.resources -= building.cost
            #Add building to list of harvesting buldings
            self.owned_buildings.append(building)
            self.resources += building.resource_output
            # print(f"{self.name} purchased {building.name}")
        # else:
            # print(f"{self.name} has insufficient resources to buy {building.name}")
            




    def fire_power(self):
        return self.att.all_units()
    
    def all_materials(self):
        return self.res.all_resources()