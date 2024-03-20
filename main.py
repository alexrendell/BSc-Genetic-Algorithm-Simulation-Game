from village import Village
from algorithm import Algorithm

def main():
    
    #Generation parameters:
    test_generation = Algorithm(200, #Number of turns
                                50, #Population size
                                100, #Number of generations
                                ({"food":5000,"wood":5000,"stone":5000,"metal":5000,"gold":0}), #Starting resources
                                10) #Starting workers
    # Mutation rate, Tournament selection sizes
    test_generation.run_genetic_algorithm(0.05,5)
    
    print(test_generation)
    
if __name__ == "__main__":
    main()


# Command + / - to comment and uncomment