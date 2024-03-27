class Troop:
    def __init__(self,name,cost,attack_output):
        self.name = name
        self.cost = cost
        self.attack_output = attack_output
    

all_troops = [
    Troop("SKIP",
             {},
             {}),
    Troop("Swordsman",
             {"food":200, "wood":250},
             {"Strength":8, "speed":15, "adaptability":10, "special ability": 0}),
    Troop("Archer",
             {"food":200, "wood":350, "stone":250},
             {"Strength":4, "speed":25, "adaptability":10, "special ability": 0}),
    Troop("Knight",
             {"food":250, "wood":200, "stone":400, "metal":150, "gold":5},
             {"Strength":20, "speed":10, "adaptability":30, "special ability": 2}),
    Troop("Siege Machine", 
             {"food":400, "wood":400, "stone":600, "metal":500, "gold":15},
             {"Strength":40, "speed":2, "adaptability":6, "special ability": 5}),
    Troop("Scout", 
             {"food":400, "wood":400, "stone":600, "metal":500, "gold":15},
             {"Strength":6, "speed":35, "adaptability":20, "special ability": 0}),
    Troop("Pope",
             {"food":200, "gold":200},
             {"Strength":2, "speed":10, "adaptability":5, "special ability": 1}),
    Troop("Op",
              {},
              {"Strength":1000, "speed":1000, "adaptability":1000, "special ability": 1000}),
]