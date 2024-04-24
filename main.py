from village import Village
from algorithm import Algorithm

def main():
    
    #Generation parameters:
    test_generation = Algorithm(20, #Number of resource gathering turns
                                10, #Number of attacking turns
                                40, #Population size
                                10000, #Number of generations
                                ({"food":10,"wood":10,"stone":10,"metal":0,"gold":0}), #Starting resources
                                5) #Starting workers
    # Mutation rate, Tournament selection sizes
    test_generation.run_genetic_algorithm(0.05,5)
    
    print(test_generation)
    
if __name__ == "__main__":
    main()


# Command + / - to comment and uncomment