class Building:
    def __init__(self,name,cost,resource_output):
        self.name = name
        self.cost = cost
        self.resource_output = resource_output
    
    
'''    
all_buildings = [
    Building("SKIP", 0, 0), #Does cost or give anything just skips a round insetad of failing to buy a resouce
    Building("Worker", 20, 3),
    Building("Farm", 70, 10),
    Building("mine", 60, 25),
    Building("Lumber Mill",10, 100)
]
'''    
    
all_buildings2 = [
    Building("SKIP", 
             {"food":0, "wood":0, "stone":0, "metal":0, "gold":0}, 
             {"food":0, "wood":0, "stone":0, "metal":0, "gold":0}),
    Building("Worker",
             {"food":5, "wood":0, "stone":0, "metal":0, "gold":0},
             {"food":2, "wood":1, "stone":1, "metal":0, "gold":0}),
    Building("Farm",
             {"food":20,"wood":10, "stone":10, "metal":0, "gold":0},
             {"food":10, "wood":4, "stone":2, "metal":0, "gold":0}),
    Building("Lumber Mill",
             {"food":50, "wood":100, "stone":25, "metal":0, "gold":0},
             {"food":2, "wood":20, "stone":4, "metal":0, "gold":0}),
    Building("Quarry", 
             {"food":100, "wood":150, "stone":50, "metal":0, "gold":0},
             {"food":4, "wood":4, "stone":20, "metal":4, "gold":0}),
    Building("Forge",
             {"food":150, "wood":200, "stone":80, "metal":0, "gold":0},
             {"food":2, "wood":2, "stone":4, "metal":20, "gold":0}),
    Building("Op",
             {"food":0, "wood":0, "stone":0, "metal":0, "gold":0},
             {"food":1000, "wood":1000, "stone":1000, "metal":1000, "gold":1000}),
]

