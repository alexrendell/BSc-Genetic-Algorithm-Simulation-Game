class Upgrade:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost

all_upgrades = [
    Upgrade("Stronger Legs",
             {"food": 0, "wood":0, "stone":0, "metal":0, "gold": 1}),
    Upgrade("Trade Routes",
             {"food":0, "wood":0, "stone":0, "metal":0, "gold":3}),
    Upgrade("Fertilizer",
             {"food":0, "wood":0, "stone":0, "metal":0, "gold":5}),
    Upgrade("Drill",
             {"food":0, "wood":0, "stone":0, "metal":0, "gold":8}),
    Upgrade("Gasoline", 
             {"food":0, "wood":0, "stone":0, "metal":0, "gold":10}),
    Upgrade("Golden Pickaxe", 
             {"food":0, "wood":0, "stone":0, "metal":0, "gold":15})
]
