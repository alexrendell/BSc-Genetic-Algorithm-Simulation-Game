class GeneticAlgorithm:
    
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        
    def evaluate_fitness(village):
        resource_fitness = #calculate_resource_fitness(village)
        attcking_fitness = #calculate_combat_fitness(village)
        defendive_fitness = #calculate_defensive_fitness(village)
        overall_fitness = (0.4 * resource_fitness) + (0.3 * attcking_fitness)
        + (0.3 * defendive_fitness) # weight is adjusted by priority
        
        return overall_fitness

    # Calculate fitness based on resource gathering efficiency
    def calculate_resource_fitness(village):
        return village.total_resources_gathered
 
    # Calculate fitness based on attacking performance
    def calculate_Attacking_fitness(village):
        return (village.successful_attacks)
    
    # Calculate fitness based on defensive performance
    def calculate_defensive_fitness(village):
        return (village.successful_defenses)