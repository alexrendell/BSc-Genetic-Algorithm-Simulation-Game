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
             {"food":200, "wood":300},
             {"strength":500, "speed":900, "adaptability":600, "special ability": 0}),
    Troop("Archer",
             {"food":250, "wood":350, "stone":200},
             {"strength":300, "speed":900, "adaptability":600, "special ability": 0}),
    Troop("Knight",
             {"food":300, "wood":200, "stone":400, "metal":250, "gold":10},
             {"strength":600, "speed":100, "adaptability":500, "special ability": 100}),
    Troop("Siege Machine", 
             {"food":400, "wood":400, "stone":500, "metal":40, "gold":10},
             {"strength":500, "speed":1150, "adaptability":550, "special ability": 300}),
    Troop("Scout", 
             {"food":500, "wood":0, "stone":600, "metal":100, "gold":20},
             {"strength":150, "speed":1500, "adaptability":500, "special ability": 0}),
    Troop("Pope",
             {"food":150, "gold":50},
             {"strength":100, "speed":500, "adaptability":250, "special ability": 500}),
    #Troop("Pope2",
             #{"food":0, "gold":0},
             #{"strength":200, "speed":200, "adaptability":200, "special ability": 200}),
]