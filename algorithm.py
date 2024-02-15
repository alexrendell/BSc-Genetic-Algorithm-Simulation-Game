import random
from village import Village
from Thesis2.buildings import Building

class Algorithm:
    def __init__(self, strategy, population, generation):
        self.strategy = strategy
        self.population = population
        self.generation = generation
        self.all_buildings = Building.all_buildings
        
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
        
        #Calculate total resources gathered by temp village   
        total_resources = sum([building.resource_output.get(resource, 0) 
                               for building in temp_village.owned_buildings 
                               for resource in building.resource_output])
        return total_resources
    
    #Selects parents for crossover base don their fitness
    def select_parents(self, population, num_parents):
        #Use all individuals in the population as parents
        parents = population
        #Sort strategies based on fittness in decending order
        parents.sort(key=lambda strategy: self.evaluate_fitness(strategy))
        #Reverse to highest to lowest
        parents.reverse()
        #Return the top 'num_parents' strategies as parents
        sorted_parents = parents[:num_parents]
        return sorted_parents
    
    #Preforms crossover to create a new offspring
    def crossover1(self, parent1, parent2):
        #Randomly selects a point from the range 1 to length -1
        crossover_point = random.randint(1, len(parent1) - 1)
        #The begining of the childs stretegy up to the crossover point is from parent 1 and the rest is from parent 2
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child
    
    def crossover2(self, parent1, parent2):
        #Randomly selects a point from the range 1 to length -1
        crossover_point = random.randint(1, len(parent1) - 1)
        #The begining of the childs stretegy up to the crossover point is from parent 1 and the rest is from parent 2
        child = parent2[:crossover_point] + parent1[crossover_point:]
        return child
    
    #Apply mutation to a strategy
    def mutate(self, strategy, mutation_rate):
        #Creates a copy of the original strategy to avoid changing the original
        mutated_strategy = strategy.copy()
        #Loops through all the buildings in strategy
        for i in range(len(mutated_strategy)): #range starts from 0 and increments 1 untill length of mutated strategy
            #genrates a random float from 0.00 - 1.00 if it is less than the mutation rate it mutates
            if random.random() < mutation_rate:
                #changes one of the buildings in strategy to another random building
                mutated_strategy[i] = random.choice(range(len(self.all_buildings)))
            
        return mutated_strategy
    
    def evolve_population(self, current_population, mutaiton_rate):
        
        new_population = []
        num_parents = 5
        
        
        
        
    