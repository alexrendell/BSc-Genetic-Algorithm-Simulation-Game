'''
from village import Village
import algorithm
from resources import Resources

res = Resources

instance1 = Village("Rhondda", 47000)
instance2 = Village("Merthyr", 100000)

print(instance1.all_materials())
print(instance1.fire_power())

ranked = []

ranked = algorithm.all_villages

#print(ranked)
'''

from village import Village
from algorithm import Algorithm

def main():
    
    village_a = Village("village A", 100, 10)
    village_b = Village("village B", 80, 8)
    
    village_a.buy_building(1)
    village_a.buy_building(2)
    
    print("##########################")
    
    test_generation = Algorithm(20, 13, 5)
    
    print(test_generation)
    
if __name__ == "__main__":
    main()

