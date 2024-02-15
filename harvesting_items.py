class Harvesting:
    def __init__(self,name,cost,resource_output):
        self.name = name
        self.cost = cost
        self.resource_output = resource_output
    
all_buildings = [
    Harvesting("Worker", 20, {"food:":1, "stone":1, "wood":1}),
    Harvesting("Farm", 70, {"food":5}),
    Harvesting("mine", 60, {"stone":3}),
    Harvesting("Lumber Mill", 60, {"wood":4})
]


def buy_farm(self):
    farm = farm + 1
        