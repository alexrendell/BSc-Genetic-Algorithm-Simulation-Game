import random

all_villages = []
#all_villages.sort(key=lambda x: x[1])
#all_villages.reverse()


def fitness(name, total_resources):
    
    #total_resources = wood + coal + metal + gold
    
    all_villages.append( (name,total_resources) )