#USED UMGPT for structure and logic 
class Player: 
    def __init__(self, name, cash=1500): 
        self.name = name 
        self.cash = cash 
        self.current_space = 0 
        self.owned_properties = [] 
        self.in_jail = False 
 
#USED UMGPT for movement logic 
    def move(self, steps, board_size): 
        if not self.in_jail: 
            self.current_space = (self.current_space + steps) %% board_size 
        else: 
            self.cash -= 50 
            self.in_jail = False 
 
#USED UMGPT for basic class formatting 
class Property: 
    def __init__(self, name, purchase_price, rent): 
        self.name = name 
        self.purchase_price = purchase_price 
        self.rent = rent 
        self.owner = None 
