from village import Village
from algorithm import Algorithm

def main():
    
    #Generation parameters:
    test_generation = Algorithm(100, #Number of turns
                                40, #Population size
                                500, #Number of generations
                                ({"food":0,"wood":0,"stone":0,"metal":0,"gold":0}), #Starting resources
                                5) #Starting workers
    # Mutation rate, Tournament selection sizes
    test_generation.run_genetic_algorithm(0.01,5)
    
    print(test_generation)
    
if __name__ == "__main__":
    main()


# Command + / - to comment and uncomment