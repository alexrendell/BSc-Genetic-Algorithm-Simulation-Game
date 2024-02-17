class Building:
    def __init__(self,name,cost,resource_output):
        self.name = name
        self.cost = cost
        self.resource_output = resource_output
    
    
all_buildings = [
    Building("Worker", 20, {"food:":1, "stone":1, "wood":1}),
    Building("Farm", 70, {"food":5}),
    Building("mine", 60, {"stone":3}),
    Building("Lumber Mill", 60, {"wood":4})
]
