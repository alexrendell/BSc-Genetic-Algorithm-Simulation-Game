import random
from village import Village
import buildings
import troops
import numpy.random as npr
import copy
import upgrades

class Algorithm:
    #Strategy is the amount of moves / buildings that can be bought
    def __init__(self, resource_turns, attack_turns, population_size, generations, starting_resources, starting_workers):  #Change strategy to turns 
        self.resource_turns = resource_turns
        self.attack_turns = attack_turns
        self.population_size = population_size
        self.generations = generations
        self.all_buildings = buildings.all_buildings
        self.all_troops = troops.all_troops
        self.all_upgrades = upgrades.all_upgrades
        self.starting_resources = starting_resources
        self.starting_workers = starting_workers
        self.i = 0
        self.current_best = None
        
    #Creates the first poplation with random strategies
    def initialize_population(self):
        population = []
        
        for agent in range(self.population_size):
            building_strategy = []
            #Assignes a valid gene to each element of first strategy
            for building in range(self.resource_turns):
                action = random.randint(0,1)
                #Purchase of a buildig
                if action == 0:
                    building_number = random.randint(0, len(self.all_buildings)-1)
                    building_strategy.append((0, building_number))
                #Purchase of an upgrade
                else:
                    upgrade_number = random.randint(0, len(self.all_upgrades)-1)
                    building_strategy.append((1, upgrade_number))
                    
            #Assignes a gene for each element of the second strategy
            troop_strategy = [self.all_troops.index(troop) for troop in random.choices(self.all_troops, k=self.attack_turns)] 
            #Add the strategy to a child and add the child to the population
            population.append((building_strategy,troop_strategy))
            
        return population
    
    #Evaluates each agent and returns a fitness value
    def evaluate_fitness(self, strategy):
        total_resources = 0
        building_strategy = strategy[0]
        troop_strategy = strategy[1]
        starting_resources = copy.deepcopy(self.starting_resources)
        starting_workers = self.starting_workers
        
        #Resource colleciton (phase 1)
        temp_village = Village("Temp_Village", starting_resources, starting_workers)
        for building in building_strategy:
            temp_village.buy_building(building)
        
        #Troop purchasing (phase 2)
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
        #Combining segments from both parents
        child_building = parent1[0][:building_crossover_point]+ parent2[0][building_crossover_point:]
        child_troop = parent1[1][:troop_crossover_point]+ parent2[1][troop_crossover_point:]
        #Combine both segments into a single new agent
        child = (child_building, child_troop)
        return child
        
    
    #Apply mutation to a strategy
    def mutate(self, strategy, mutation_rate):
        #Creates a copy of the original strategy to avoid changing the original
        mutated_building_strategy = strategy[0].copy()
        mutated_troop_strategy = strategy[1].copy()
        #Loops through all the buildings in strategy
        for building in range(len(mutated_building_strategy)):
            # If mutaiton occurs it changes the action
            if random.random() < mutation_rate:
                action, value = mutated_building_strategy[building]
                if action == 1:
                    action = 0
                    value = random.choice(range(len(self.all_buildings)))
                else:
                    action = 1
                    value = random.choice(range(len(self.all_upgrades)))
                mutated_building_strategy[building] = (action, value)
                    
        
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
    
    #Seleciton method using probability
    def roulette_wheel(self, current_population):
        
        highest_first_fitness = [self.evaluate_fitness(building_strategy) for building_strategy in current_population]
        
        total_fitness = sum(highest_first_fitness)
        #Calculate probability of being chosen based on fitness values
        probability = [fitness / total_fitness for fitness in highest_first_fitness]
        #Choose a single agent from popualtion 
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
            best_attack_strategy = best_of_population[1]
            
            for building in best_building_strategy:
                best_village.buy_building(building)
                
            for troop in best_attack_strategy:
                best_village.buy_troop(troop)
            
            best_fitness = self.evaluate_fitness(best_of_population)
            best_food = best_village.get_food()
            best_wood = best_village.get_wood()
            best_stone = best_village.get_stone()
            best_metal = best_village.get_metal()
            best_gold = best_village.get_gold()
            best_attack = best_village.get_attack()
            best_defence = best_village.get_defence()
            res = best_village.total_resources()
            att = best_village.total_attack()
            
            print(f"Generation {generation+1}, Fitness: {best_fitness}, Attack: {best_attack}, Defence: {best_defence}")
            print(f"Food: {best_food}, Wood: {best_wood}, Stone: {best_stone}, Metal: {best_metal}, Gold: {best_gold}")
            print(f"Best resouce strategy: {best_of_population[0]}")
            print(f"Best attack strategy: {best_of_population[1]}")
            print(f"Upgrades aquired: {best_village.get_upgrades()}")
            print("")
            
            if self.current_best == None or best_fitness > self.current_best:
                self.current_best = best_fitness
        
            print(f"total res: {res}")
            print(f"total attack: {att}")
            print()
        
            if generation % 20 ==0:
                with open("tou=5_pun=10%_mut=5%.csv","a") as file:
                    file.write(f"{best_fitness}\n")        
        
        print(f"Best Fitness Overall: {self.current_best}")
            