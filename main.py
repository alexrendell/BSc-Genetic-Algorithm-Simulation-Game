from village import Village
from algorithm import Algorithm

def main():
    
    #Generation parameters:
    #number or turns, population size, maximum number of generations, starting resources, starting workers
    test_generation = Algorithm(40, 50, 100, 10000, 10)
    # Mutation rate, Tournament selection size
    test_generation.run_genetic_algorithm(0.05,5)
    
    print(test_generation)
    
if __name__ == "__main__":
    main()


# Command + / - to comment and uncomment