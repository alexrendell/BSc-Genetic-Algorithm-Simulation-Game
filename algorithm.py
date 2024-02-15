import random
from village import Village
from buildings import Building

class Algorithm:
    def __init__(self, strategy, population, generation):
        self.strategy = strategy
        self.population = population
        self.generation = generation
        
    def initialize_population(self):
        population = []
        for strategy in range(self.population_size):
            #Generate random strategy
            strategy = random.sample(self.all_buildings, len(self.buildings))
            population.append(strategy)
        return population
    
    def evaluate_fitness(self, village, strategy):
        #need to make villae return a instance of village class
        total_resources = 0
        
        #Creates a temporary village to simulate strtegy
        temp_village = Village("temp", 100, 10)
        
        #Purchase buildings according to strategy
        for building_number in strategy:
            temp_village.buy_building(building_number)
            
        total_resources = sum([building.resource_output.get(resource, 0) 
                               for building in temp_village.owned_buildings 
                               for resource in building.resource_output])
        return total_resources
    
    