#USED UMGPT for structure and logic 
class Player: 
    def __init__(self, name, cash=1500): 
        self.name = name 
        self.cash = cash 
        self.current_space = 0 
        self.owned_properties = [] 
        self.in_jail = False 
