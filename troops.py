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
             {"food":20, "wood":30},
             {"strength":100, "speed":180, "adaptability":120, "special ability": 0}),
    Troop("Archer",
             {"food":25, "wood":35, "stone":20},
             {"strength":60, "speed":180, "adaptability":125, "special ability": 0}),
    Troop("Knight",
             {"food":30, "wood":20, "stone":40, "metal":25, "gold":1},
             {"strength":125, "speed":20, "adaptability":100, "special ability": 20}),
    Troop("Siege Machine", 
             {"food":40, "wood":40, "stone":50, "metal":40, "gold":1},
             {"strength":100, "speed":25, "adaptability":75, "special ability": 65}),
    Troop("Scout", 
             {"food":50, "wood":0, "stone":60, "metal":10, "gold":2},
             {"strength":30, "speed":300, "adaptability":100, "special ability": 0}),
    Troop("Pope",
             {"food":15, "gold":5},
             {"strength":20, "speed":100, "adaptability":50, "special ability": 50}),
    #Troop("Pope2",
             #{"food":0, "gold":0},
             #{"strength":100000, "speed":100000, "adaptability":100000, "special ability": 100000}),
]