class Upgrade:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost

all_upgrades = [
    Upgrade("Stronger Legs",
             {"food": 500, "wood":500, "stone":500, "metal":500, "gold": 1}),
    Upgrade("Trade Routes",
             {"food":1000, "wood":1000, "stone":1000, "metal":1000, "gold":3}),
    Upgrade("Fertilizer",
             {"food":1500, "wood":1500, "stone":1500, "metal":1500, "gold":5}),
    Upgrade("Drill",
             {"food":2000, "wood":2000, "stone":2000, "metal":2000, "gold":8}),
    Upgrade("Gasoline", 
             {"food":2500, "wood":2500, "stone":2500, "metal":2500, "gold":10}),
    Upgrade("Golden Pickaxe", 
             {"food":3000, "wood":3000, "stone":3000, "metal":3000, "gold":15})
]
