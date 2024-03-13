class Building:
    def __init__(self,name,cost,resource_output):
        self.name = name
        self.cost = cost
        self.resource_output = resource_output
    
    
    
all_buildings = [
    Building("SKIP", 0, 0), #Does cost or give anything just skips a round insetad of failing to buy a resouce
    Building("Worker", 20, 3),
    Building("Farm", 70, 10),
    Building("mine", 60, 25),
    Building("Lumber Mill",10, 100)
]
    
'''    Multiple resources (maye incorprate later)
all_buildings = [
    Building("SKIP", 0, {}), #Does cost or give anything just skips a round insetad of failing to buy a resouce
    Building("Worker", 20, {"food:":1, "stone":1, "wood":1}),
    Building("Farm", 70, {"food":5}),
    Building("mine", 60, {"stone":3}),
    Building("Lumber Mill", 60, {"wood":4})
]
'''
