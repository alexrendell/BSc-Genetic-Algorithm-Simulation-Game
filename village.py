from resources import Resources
import buildings as buildings
import troops as troops


class Village:
    def __init__(self, name, resources, workers):
        self.name = name
        self.workers = workers
        self.resource_balance = resources
        self.resource_income = ({"food":0,"wood":0,"stone":0,"metal":0,"gold":0})
        self.owned_buildings = []
        self.attack_output = ({"strength":0,"speed":0,"adaptability":0,"special ability":0})
        self.owned_troops = []
        
        #Add the amount of workers to the list of owned buildings
        for buy_workers in range(workers):
            building = buildings.all_buildings[1]
            for resource, output in building.resource_output.items():
                self.resource_income[resource] += output
            self.owned_buildings.append(building)
            
        self.turn = 0
        self.defensive_strength = 100
        self.attacking_power = 100 
       
    #Purchasing a troop 
    def buy_troop(self, troop_number):
        
        troop = troops.all_troops[troop_number]
        
        if all(self.resource_balance[resource] >= troop.cost[resource]
               for resource in troop.cost):
            
            for resource, cost in troop.cost.items():
                self.resource_balance[resource] -= cost
            
            for stat, output in troop.attack_output.items():
                self.attack_output[stat] += output
                print(output)  
            
            self.owned_troops.append(troop)
            
            #If agent cant buy building it gets punished (promiting the skip building)
        else:
            for resource in self.resource_balance:
                self.resource_balance[resource] * 0.5
                    
    #Purchasing a building
    def buy_building(self, building_number):
        
        # Adds the income to their balance
        for resource, cost in self.resource_income.items():
            self.resource_balance[resource] += self.resource_income[resource]
        
        #Retruns building getting bought
        building = buildings.all_buildings[building_number]
        #Check if village has enough resources
        if all(self.resource_balance[resource] >= building.cost[resource] 
               for resource in building.cost):
            #Deducts the cost of the building
            for resource, cost in building.cost.items(): #.items returns the pair 
                self.resource_balance[resource] -= cost
            
            # Adds the output of the building to the village income
            for resource, output in building.resource_output.items():
                self.resource_income[resource] += output            #here somewhere
            
            self.attacking_and_defence(building)
            
            self.owned_buildings.append(building)
            
            #If agent cant buy building it gets punished (promiting the skip building)
        else:
            for resource in self.resource_balance:
                self.resource_balance[resource] *= 0.5
    
    def total_attack(self):
        total_attack = 0
        #strenght, speed, adaptability, special ability
        stat_weight = (1.25, 1.25, 1.25, 1.25)
        for stat, amount in self.attack_output.items():
           if stat == "strength":
               total_attack += (amount * stat_weight[0])
               #print("strenght",amount)
           elif stat == "speed":
               total_attack += (amount * stat_weight[1])
               #print("speed",amount)
           elif stat == "adaptability":
               total_attack += (amount * stat_weight[2])
               #print("adaptability", amount)
           elif stat == "special ability":
               total_attack += (amount * stat_weight[3])
               #print("special ability", amount)
                    
        return total_attack
       
    def total_resources(self):
        total_resource = 0
        for name, amount in self.resource_balance.items():
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
            total_resource += total_resource * (1 + (attack_score))
        
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
    
    def get_food(self):
        return self.resource_balance["food"]
    
    def get_wood(self):
        return self.resource_balance["wood"]
    
    def get_stone(self):
        return self.resource_balance["stone"]
    
    def get_metal(self):
        return self.resource_balance["metal"]
    
    def get_gold(self):
        return self.resource_balance["gold"]