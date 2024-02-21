import random
from village import Village
import buildings

class Algorithm:
    #Strategy is the amount of moves / buildings that can be bought
    def __init__(self, turns, population_size, generations, starting_resources, starting_workers):  #Change strategy to turns 
        self.turns = turns
        self.population_size = population_size
        self.generations = generations
        self.all_buildings = buildings.all_buildings
        self.starting_resources = starting_resources
        self.starting_workers = starting_workers
        self.i = 0
        
    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            #Generate random strategy of length turns (the number of turns)
            #choices picks random elements from the all_buildings list (picks self.turn amount of elements)
            #The stategy is now a list of the index of the building
            strategy = [self.all_buildings.index(building) for building in random.choices(self.all_buildings, k=self.turns)]
            #Add the strategy to a child and add the child to the population
            population.append(strategy)
        return population
    
    def evaluate_fitness(self, strategy):
        #need to make villae return a instance of village class
        total_resources = 0
        
        #Creates a temporary village to simulate strtegy
        temp_village = Village(f"Village {self.i}", self.starting_resources, self.starting_workers)
        if self.i > self.population_size:
            self.i = 0
        else:
            self.i += 1
        
        #Purchase buildings according to strategy
        for building_number in strategy:
            temp_village.buy_building(building_number)
        
        #Calculate total resources of all buildings
        for building in temp_village.owned_buildings:
                total_resources += building.resource_output
            
            
        ''' find the total resouce when there are multiple
        #Calculate total resources gathered by temp village  
        total_resources = sum([building.resource_output.get(resource, 0) 
                               for building in temp_village.owned_buildings 
                               for resource in building.resource_output])
        '''
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
    def crossover(self, parent1, parent2):
        #Randomly selects a point from the range 1 to length -1
        crossover_point = random.randint(1, len(parent1) - 1)
        #The begining of the childs stretegy up to the crossover point is from parent 1 and the rest is from parent 2
        child = parent1[:crossover_point] + parent2[crossover_point:]
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
    
    #Combines oarents through crossover and muation
    def evolve_population(self, current_population, mutation_rate):
        
        new_population = []
        num_parents = 3
        
        #Selects the top number of parents
        top_parents = self.select_parents(current_population, num_parents)
        print(top_parents)
        #The combinations of the children for next generation
        combinations = [
            (top_parents[0], top_parents[1], 2),
            (top_parents[1], top_parents[0], 2),
            (top_parents[0], top_parents[2], 2),
            (top_parents[2], top_parents[0], 2),
            (top_parents[1], top_parents[2], 1),
            (top_parents[2], top_parents[1], 1)
        ]
        
        #Generate the new generation of children
        for parent1, parent2, num_children in combinations:
            #Check how much children are needed from the parents
            for _ in range(num_children):
                #Crossover the parents and create a new child
                child = self.crossover(parent1, parent2)
                #Mutate the child
                mutated_child = self.mutate(child, mutation_rate)
                #Add the child to the list of new population
                new_population.append(mutated_child)
            #Keep the orignal 3 parents in the new population
            new_population.extend(top_parents)
            
        return new_population
        
     #Starting the genetic algorithm
    #None means that the parameter is optional
    def run_genetic_algorithm(self, initial_population = None, mutation_rate = 0.01):
                    
        #If its the first generation the get the first population
        if initial_population is None:
            current_population = self.initialize_population()
        #Otherwise use the current population
        else:
           current_population = initial_population
            
        #Loop over each generation
        for generation in range(self.generations):
            print(F"Generation {generation + 1}")
            
            #Evaluate and print the fitness of each strategy in the current population
            for strategy in current_population:
                fitness = self.evaluate_fitness(strategy)
                print("fStrategy: {strategy}, Fitness: {fitness}")
                
        #Create the population for the next generation
        current_population = self.evolve_population(current_population, mutation_rate)
        
        #return whatever i need, here its the current popoulation
        return current_population
            
        
        
        #populaiton of 12
        #1 = 1
        #2 = 1
        #3 = 1
        #1&2, 2&1 * 2 = 4
        #1&3, 3&1 * 2 = 4
        #2&3. 2&3 = 2
        #total of 13 children 