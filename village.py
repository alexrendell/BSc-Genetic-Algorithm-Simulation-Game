from resources import Resources
import buildings as buildings


class Village:
    def __init__(self, name, resources, workers):
        self.name = name
        self.workers = workers
        self.resources_count = resources
        self.owned_buildings = []
        #Add the amount of workers to the list of owned buildings
        for buy_workers in range(workers):
            self.owned_buildings.append(buildings.all_buildings2[1])
        self.turn = 0
        
    #Purchasing a building
    def buy_building(self, building_number):
        #Retruns building getting bought
        building = buildings.all_buildings2[building_number]
        #Check if village has enough resources
        if all(self.resources_count[resource] >= building.cost[resource] 
               for resource in building.cost):
            for resource, cost in building.cost.items(): #.items returns the pair 
                self.resources_count[resource] -= cost
            
            self.owned_buildings.append(building)
            
            for resource, output in building.resource_output.items():
                self.resources_count[resource] += output
       
    def total_resources(self):
        total_resource = 0
        for name, amount in self.resources_count.items():
            if name == "food":
                total_resource += amount
            elif name == "wood":
                total_resource += (amount * 1.5)
            elif name == "stone":
                total_resource += (amount * 2)
            elif name == "metal":
                total_resource += (amount * 5)
            elif name == "gold":
                total_resource += (amount * 100)
                
                
        return total_resource
                
        
       

        # if self.resources >= building.cost:
        #     #Deduct cost from village resources
        #     self.resources -= building.cost
        #     #Add building to list of harvesting buldings
        #     self.owned_buildings.append(building)
        #     self.resources += building.resource_output
        #     # print(f"{self.name} purchased {building.name}")
        # # else:
        #     # print(f"{self.name} has insufficient resources to buy {building.name}")     



    def fire_power(self):
        return self.att.all_units()
    
    def all_materials(self):
        return self.res.all_resources()