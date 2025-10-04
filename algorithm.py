import random
from village import Village
import buildings
import numpy.random as npr
import copy

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
        total_resources = 0
        #Creating a deep copy because i dont want the original starting resources 
        #to be changed and its a dictionary so it will always reference the original starting_resoruces
        test_starting_resources = copy.deepcopy(self.starting_resources)
        test_starting_workers = self.starting_workers
        
        temp_village = Village("Temp_Village", test_starting_resources, test_starting_workers)
        for building in strategy:
            temp_village.buy_building(building)
        
        #total_resources = temp_village.total_resources()
        total_resources = temp_village.total_fitness()
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
        
        crossover_point = random.randint(1, len(parent1) -1)
        
        child = parent1[:crossover_point] + parent2[crossover_point:]
        
        return child
        
    
    #Apply mutation to a strategy
    def mutate(self, strategy, mutation_rate):
        #Creates a copy of the original strategy to avoid changing the original
        mutated_strategy = strategy.copy()
        #Loops through all the buildings in strategy
        for building in range(len(mutated_strategy)): #range starts from 0 and increments 1 untill length of mutated strategy
            #genrates a random float from 0.00 - 1.00 if it is less than the mutation rate it mutates
            if random.random() < mutation_rate:
                #changes one of the buildings in strategy to another random building
                mutated_strategy[building] = random.choice(range(len(self.all_buildings)))
            
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
        
        highest_first_fitness = [self.evaluate_fitness(strategy) for strategy in current_population]
        
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
        
            # Evaluate the fitness of each individual in the tournament
            tournament_fitness = [self.evaluate_fitness(potential_parent) for potential_parent in tournament_parents]
        
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
                
                # parent_1 = self.roulette_wheel(current_population)
                # parent_2 = self.roulette_wheel(current_population)
                
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
            for building in best_of_population:
                best_village.buy_building(building)
            
            best_fitness = self.evaluate_fitness(best_of_population)
            best_food = best_village.get_food()
            best_wood = best_village.get_wood()
            best_stone = best_village.get_stone()
            best_metal = best_village.get_metal()
            best_gold = best_village.get_gold()
            
            print(f"Generation {generation+1}, Fitness: {best_fitness}")
            print(f"Food, {best_food}, Wood, {best_wood}, Stone, {best_stone}, Metal: {best_metal}, Gold: {best_gold}")
            print(best_of_population)    
            
            if generation %2==1:
                with open("Fair.csv", "a") as file:
                    file.write(f"{generation} , {best_fitness}\n")
        
            
        
        
        #populaiton of 12
        #1 = 1
        #2 = 1
        #3 = 1
        #1&2, 2&1 * 2 = 4
        #1&3, 3&1 * 2 = 4
        #2&3. 2&3 = 2
        #total of 13 children 