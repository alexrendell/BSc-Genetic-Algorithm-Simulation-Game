from village import Village
from algorithm import Algorithm

def main():
    print("##########################")
    
    #Generation parameters:
    #number or turns, population size, maximum number of generations, starting resources, starting workers
    test_generation = Algorithm(10, 13, 500000, 300, 10)
    test_generation.run_genetic_algorithm()
    
    print(test_generation)
    
if __name__ == "__main__":
    main()


# Command + / - to comment and uncomment