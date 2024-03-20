class Building:
    def __init__(self,name,cost,resource_output,attacking_power=0,defensive_strength=0):
        self.name = name
        self.cost = cost
        self.resource_output = resource_output
        self.attacking_power = attacking_power
        self.defensive_strength = defensive_strength
    

all_buildings = [
    Building("SKIP",
             {},
             {}),
    Building("Worker",
             {"food":5,},
             {"food":2, "wood":1, "stone":1,}),
    Building("Farm",
             {"food":20,"wood":10, "stone":10},
             {"food":10, "wood":4, "stone":2}),
    Building("Lumber Mill",
             {"food":50, "wood":100, "stone":25},
             {"food":2, "wood":20, "stone":4}),
    Building("Quarry", 
             {"food":100, "wood":150, "stone":50},
             {"food":4, "wood":4, "stone":20, "metal":4}),
    Building("Forge",
             {"food":150, "wood":200, "stone":80},
             {"food":2, "wood":2, "stone":4, "metal":20}),
    Building("Op",
             {},
             {"food":1000, "wood":1000, "stone":1000, "metal":1000, "gold":1000}),
    Building("Defence",
             {"food":1},
             {},
             0,1),
    Building("Attack",
             {"food":1},
             {},
             1,0),
]

