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
             {"food":100, "wood":125},
             {"strength":8, "speed":15, "adaptability":10, "special ability": 0}),
    Troop("Archer",
             {"food":100, "wood":175, "stone":125},
             {"strength":4, "speed":25, "adaptability":10, "special ability": 0}),
    Troop("Knight",
             {"food":125, "wood":100, "stone":200, "metal":75, "gold":0},
             {"strength":20, "speed":10, "adaptability":30, "special ability": 2}),
    Troop("Siege Machine", 
             {"food":200, "wood":200, "stone":300, "metal":250, "gold":5},
             {"strength":40, "speed":2, "adaptability":6, "special ability": 5}),
    Troop("Scout", 
             {"food":200, "wood":200, "stone":300, "metal":250, "gold":5},
             {"strength":6, "speed":35, "adaptability":20, "special ability": 0}),
    Troop("Pope",
             {"food":100, "gold":20},
             {"strength":2, "speed":10, "adaptability":5, "special ability": 1}),
]