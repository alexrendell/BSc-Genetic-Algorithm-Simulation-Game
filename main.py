from village import Village
from algorithm import Algorithm

def main():
    print("##########################")
    
    #Generation parameters:
    #number or turns, population size, maximum number of generations, starting resources, starting workers
    test_generation = Algorithm(20, 50, 500, 1000, 10)
    # Mutation rate
    test_generation.run_genetic_algorithm(0.05)
    
    print(test_generation)
    
if __name__ == "__main__":
    main()


# Command + / - to comment and uncomment