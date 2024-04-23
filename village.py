from resources import Resources
import buildings as buildings
import troops as troops
import upgrades as upgrades


class Village:
    def __init__(self, name, resources, workers):
        self.name = name
        self.workers = workers
        self.resource_balance = resources
        self.resource_income = ({"food":0,"wood":0,"stone":0,"metal":0,"gold":0})
        self.owned_buildings = []
        self.attack_output = ({"strength":0,"speed":0,"adaptability":0,"special ability":0})
        self.owned_troops = []
        self.owned_upgrades = []
        self.stronger_legs = False
        self.trade_routes = False
        self.fertilizer = False
        self.drill = False
        self.gasoline = False
        self.golden_pickaxe = False
        self.all_upgrades = [self.stronger_legs, self.trade_routes, self.fertilizer, self.drill, self.gasoline, self.golden_pickaxe]
        self.total_resource = 0
        self.count = 0
        
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
            
            self.owned_troops.append(troop)
            
            #If agent cant buy building it gets punished (promiting the skip building)
        else:
            for stat in self.attack_output:
                self.attack_output[stat] *= 0.9
                    
    #Purchasing a building
    def buy_building(self, building_number):
        # Adds the income to their balance
        for resource, cost in self.resource_income.items():   #This should be amount not cost.
            self.resource_balance[resource] += self.resource_income[resource]
        
        #Building
        if building_number[0] == 0:
        
            #Retruns building getting bought
            building = buildings.all_buildings[building_number[1]]
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
                    self.resource_balance[resource] *= 0.9
        
        #Upgrading
        else:
            upgrade = upgrades.all_upgrades[building_number[1]]
            
            if all(self.resource_balance[resource] >= upgrade.cost[resource] 
                for resource in upgrade.cost):
                #Deducts the cost of the building
                for resource, cost in upgrade.cost.items(): #.items returns the pair 
                    self.resource_balance[resource] -= cost
                
                self.owned_upgrades.append(upgrade)
                
                self.apply_upgrade(upgrade)  
            
            else:
                for resource in self.resource_balance:
                    self.resource_balance[resource] *= 0.9
                
    
    def total_attack(self):
        total_attack = 0
        #strenght, speed, adaptability, special ability
        stat_weight = (1.25, 1.25, 1.25, 1.25)
        for stat, amount in self.attack_output.items():
            #print (f"stat: {stat}, amount: {amount}")
            if stat == "strenght":
               total_attack += (amount * stat_weight[0])
            elif stat == "speed":
               total_attack += (amount * stat_weight[1])
            elif stat == "adaptability":
               total_attack += (amount * stat_weight[2])
            elif stat == "special ability":
               total_attack += (amount * stat_weight[3])
                    
        #print(total_attack)
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
            
            #print(total_resource)
                
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
        
        self.total_resources = total_resource
                                                                                                                                                                                                                                                                                                                                                    
        return total_resource
    
    def apply_upgrade(self, upgrade):
            if upgrade.name == "Stronger Legs":
                self.stronger_legs = True
            if upgrade.name == "Trade Routes":
                self.trade_routes = True
            if upgrade.name == "Fertilizer":
                self.fertilizer = True
            if upgrade.name == "Drill":
                self.drill = True
            if upgrade.name == "Gasoline":
                self.gasoline = True 
            if upgrade.name == "Golden Pickaxe":
                self.golden_pickaxe = True 
        
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
    
    def get_upgrades(self):
        upgrade_list = {
            "Stronger Legs": self.stronger_legs,
            "Trade Routes": self.trade_routes,
            "Fertilizer": self.fertilizer,
            "Drill": self.drill,
            "Gasoline": self.gasoline,
            "Golden Pickaxe": self.gasoline
        }
        return upgrade_list
    
    def get_total_resource(self):
        return self.total_resource
    
    def get_count(self):
        return self.count