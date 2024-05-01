from village import Village
from algorithm import Algorithm

def main():
    
    #Generation parameters: 
    test_generation = Algorithm(30, #Number of resource gathering turns
                                15, #Number of attacking turns
                                40, #Population size
                                500, #Number of generations
                                ({"food":10,"wood":10,"stone":10,"metal":0,"gold":0}), #Starting resources
                                10) #Starting workers
    # Mutation rate, Tournament selection sizes
    test_generation.run_genetic_algorithm(0.06,10)
    
if __name__ == "__main__":
    main()
