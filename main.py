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
