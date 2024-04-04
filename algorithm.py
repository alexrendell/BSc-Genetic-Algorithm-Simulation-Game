import random
from village import Village
import buildings
import troops
import numpy.random as npr
import copy

class Algorithm:
    #Strategy is the amount of moves / buildings that can be bought
    def __init__(self, resource_turns, attack_turns, population_size, generations, starting_resources, starting_workers):  #Change strategy to turns 
        self.resource_turns = resource_turns
        self.attack_turns = attack_turns
        self.population_size = population_size
        self.generations = generations
        self.all_buildings = buildings.all_buildings
        self.all_troops = troops.all_troops
        self.starting_resources = starting_resources
        self.starting_workers = starting_workers
        self.i = 0
        
    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            #Generate random strategy of length turns (the number of turns)
            #choices picks random elements from the all_buildings list (picks self.turn amount of elements)
            #The stategy is now a list of the index of the building
            building_strategy = [self.all_buildings.index(building) for building in random.choices(self.all_buildings, k=self.resource_turns)]
            troop_strategy = [self.all_troops.index(troop) for troop in random.choices(self.all_troops, k=self.attack_turns)] 
            #Add the strategy to a child and add the child to the population
            population.append((building_strategy,troop_strategy))
        return population
    
    def evaluate_fitness(self, strategy):
        total_resources = 0
        
        building_strategy = strategy[0]
        troop_strategy = strategy[1]
        
        #Creating a deep copy because i dont want the original starting resources 
        #to be changed and its a dictionary so it will always reference the original starting_resoruces
        test_starting_resources = copy.deepcopy(self.starting_resources)
        test_starting_workers = self.starting_workers
        
        #Resource colleciton phase (buying buildings)
        temp_village = Village("Temp_Village", test_starting_resources, test_starting_workers)
        for building in building_strategy:
            temp_village.buy_building(building)
        
        #Troop buying phase
        for troop in troop_strategy:
            temp_village.buy_troop(troop)
        
        total_attack = temp_village.total_attack()
        total_resources = temp_village.total_fitness()
        
        fitness = (total_resources * 0.25) + (total_attack * 0.75)
        
        return fitness
    
    #Selects parents for crossover base don their fitness
    def select_parents(self, population, num_parents):
        #Use all individuals in the population as parents
        parents = population
        #Sort strategies based on fittness in decending order
        parents.sort(key=lambda building_strategy: self.evaluate_fitness(building_strategy))
        #Reverse to highest to lowest
        parents.reverse()
        #Return the top 'num_parents' strategies as parents
        sorted_parents = parents[:num_parents]
        return sorted_parents
    
    #Preforms crossover to create a new offspring
    def crossover(self, parent1, parent2):
        
        building_crossover_point = random.randint(1, len(parent1[0]) -1)
        troop_crossover_point = random.randint(1, len(parent1[1]) -1)
        
        
        child_building = parent1[0][:building_crossover_point] + parent2[0][building_crossover_point:]
        child_troop = parent1[1][:troop_crossover_point] + parent2[1][troop_crossover_point:]
        
        
        
        child = (child_building, child_troop)
        
        return child
        
    
    #Apply mutation to a strategy
    def mutate(self, strategy, mutation_rate):
        #Creates a copy of the original strategy to avoid changing the original
        mutated_building_strategy = strategy[0].copy()
        mutated_troop_strategy = strategy[1].copy()
        #Loops through all the buildings in strategy
        for building in range(len(mutated_building_strategy)):
            if random.random() < mutation_rate:
                #changes one of the buildings in strategy to another random building
                mutated_building_strategy[building] = random.choice(range(len(self.all_buildings)))
        
        for troop in range(len(mutated_troop_strategy)):
            if random.random() < mutation_rate:
                mutated_troop_strategy[troop] = random.choice(range(len(self.all_troops)))
        
        mutated_strategy = (mutated_building_strategy, mutated_troop_strategy )  
        
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
        
    def roulette_wheel(self, current_population):
        
        highest_first_fitness = [self.evaluate_fitness(building_strategy) for building_strategy in current_population]
        
        total_fitness = sum(highest_first_fitness)
        
        probability = [fitness / total_fitness for fitness in highest_first_fitness]
        
        return current_population[npr.choice(len(current_population), p=probability)]
        
    def tournament_selection(self, current_population, tournament_size):
        # selected_parents = []
        population_size = len(current_population)
    
        # Perform tournament selection for each parent
        for _ in range(population_size):
            # Randomly select tournament_size individuals from the population
            tournament_parents = random.sample(current_population, tournament_size)
            
            #Use the tournament strategy
            #building_strategies = [parent[0] for parent in tournament_parents]
            
            tournament_fitness = [self.evaluate_fitness(potential_parent) for potential_parent in tournament_parents]
            
            # Evaluate the fitness of each individual in the tournament
            # tournament_fitness = [self.evaluate_fitness(building_strategy) for building_strategy in building_strategies]
        
            # Select the individual with the highest fitness as the parent
            parent = tournament_parents[tournament_fitness.index(max(tournament_fitness))]
        
            # Add the selected parent to the list
            # selected_parents.append(selected_parent)
    
        return parent
    
        
     #Starting the genetic algorithm
    #None means that the parameter is optional
    def run_genetic_algorithm(self, mutation_rate, tournament_size):
        self.tournament_size = tournament_size
        self.mutation_rate = mutation_rate

        current_population = self.initialize_population()
       
        #Loop over each generation
        for generation in range(self.generations):
            new_generation = []
            
            for agent in range (len(current_population)):
                
                # Step 1: Select two parents using the roulette wheel
                
                # Step:1.2 Select two parents using the tournament seleciton
                parent_1 = self.tournament_selection(current_population, tournament_size)
                parent_2 = self.tournament_selection(current_population, tournament_size)
                
                # Step 2: Create a new child with the two parents
                child = self.crossover(parent_1, parent_2)
                
                # Step 3: Apply mutation to the child
                mutated_child = self.mutate(child, mutation_rate)
                new_generation.append(mutated_child)
        
            # Step 3: Update for the next generation
            current_population = new_generation
            best_of_population = max(current_population, key=lambda agent: self.evaluate_fitness(agent))
            
            
            test_starting_resources = copy.deepcopy(self.starting_resources)
            test_starting_workers = self.starting_workers
            
            best_village = Village("Best Village", test_starting_resources, test_starting_workers)
            best_building_strategy = best_of_population[0]
            for building in best_building_strategy:
                best_village.buy_building(building)
            
            best_fitness = self.evaluate_fitness(best_of_population)
            best_food = best_village.get_food()
            best_wood = best_village.get_wood()
            best_stone = best_village.get_stone()
            best_metal = best_village.get_metal()
            best_gold = best_village.get_gold()
            best_attack = best_village.get_attack()
            best_defence = best_village.get_defence()
            
            print(f"Generation {generation+1}, Fitness: {best_fitness}, Attack: {best_attack}, Defence: {best_defence}")
            print(f"Food: {best_food}, Wood: {best_wood}, Stone: {best_stone}, Metal: {best_metal}, Gold: {best_gold}")
            print(f"Best resouce Strategy: {best_of_population[0]}")
            print(f"Best attack strategy: {best_of_population[1]}")
            print("")
 