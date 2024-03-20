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
            self.owned_buildings.append(buildings.all_buildings[1])
        self.turn = 0
        self.defensive_strength = 0
        self.attacking_power = 0 
        
    #Purchasing a building
    def buy_building(self, building_number):
        #Retruns building getting bought
        building = buildings.all_buildings[building_number]
        #Check if village has enough resources
        if all(self.resources_count[resource] >= building.cost[resource] 
               for resource in building.cost):
            #Deducts the cost of the building
            for resource, cost in building.cost.items(): #.items returns the pair 
                self.resources_count[resource] -= cost
            
            # Adds the output of the building to the village
            for resource, output in building.resource_output.items():
                self.resources_count[resource] += output            #here somewhere
            
            self.attacking_and_defence(building)
            
            self.owned_buildings.append(building)
            
       
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
    

    def attacking_and_defence(self,building):
        self.attacking_power += building.attacking_power
        self.defensive_strength += building.defensive_strength
        
    def total_fitness(self):
        total_resource = 0
        total_resource = self.total_resources()
        
        #Attack to gain extra resources (100 attacking power maximum)
        if self.attacking_power > 100:
            total_resource += total_resource * 2
        else:
            attack_score = self.attacking_power/100
            total_resource += total_resource * (1 + attack_score)
        
        # Defend to lose less resources
        if self.defensive_strength > 100:
            total_resource += total_resource * 1
        else:
            defence_score = self.defensive_strength/100
            total_resource = defence_score * total_resource
        
        # Turns to 0 decimal places
        total_resource = int(total_resource)
                                                                                                                                                                                                                                                                                                                                                    
        return total_resource
    
    def get_defence(self):
        best_defence = self.defensive_strength
        return best_defence
    
    def get_attack(self):
        best_attack = self.attacking_power
        return best_attack