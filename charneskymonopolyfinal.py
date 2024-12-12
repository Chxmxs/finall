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
 
#USED UMGPT for buy and rent logic 
    def buy(self, player): 
        if self.owner is None and player.cash 
            player.cash -= self.purchase_price 
            self.owner = player 
            player.owned_properties.append(self) 
 
    def pay_rent(self, player): 
        if self.owner and self.owner != player: 
            rent_amount = self.rent 
            player.cash -= rent_amount 
            self.owner.cash += rent_amount 
 
#USED UMGPT for full property list 
properties = [ 
    Property("Mediterranean Avenue", 60, 2), 
    Property("Baltic Avenue", 60, 4), 
    Property("Oriental Avenue", 100, 6), 
    Property("Vermont Avenue", 100, 6), 
    Property("Connecticut Avenue", 120, 8), 
    Property("St. Charles Place", 140, 10), 
    Property("States Avenue", 140, 10), 
    Property("Virginia Avenue", 160, 12), 
    Property("St. James Place", 180, 14), 
    Property("Tennessee Avenue", 180, 14), 
    Property("New York Avenue", 200, 16), 
    Property("Kentucky Avenue", 220, 18), 
    Property("Indiana Avenue", 220, 18), 
    Property("Illinois Avenue", 240, 20), 
    Property("Atlantic Avenue", 260, 22), 
    Property("Ventnor Avenue", 260, 22), 
    Property("Marvin Gardens", 280, 24), 
    Property("Pacific Avenue", 300, 26), 
    Property("North Carolina Avenue", 300, 26), 
    Property("Pennsylvania Avenue", 320, 28), 
    Property("Park Place", 350, 35), 
    Property("Boardwalk", 400, 50) 
] 
 
#USED UMGPT for dice roll logic 
import random 
def roll_dice(): 
    return random.randint(1, 6) + random.randint(1, 6) 
 
#USED UMGPT for initializing players 
def initialize_players(): 
    player_count = int(input("How many players? (2-8): ")) 
        print("Invalid number of players.") 
        player_count = int(input("How many players? (2-8): ")) 
    return [Player(f"Player {i+1}") for i in range(player_count)] 
 
#USED UMGPT for game loop structure 
def game_loop(): 
    players = initialize_players() 
    board_size = len(properties) 
    game_over = False 
 
    while not game_over: 
        for player in players: 
            print(f"\n{player.name}'s turn. Cash: ${player.cash}") 
            input("Press Enter to roll the dice...") 
            steps = roll_dice() 
            print(f"{player.name} rolled {steps}.") 
            player.move(steps, board_size) 
            current_property = properties[player.current_space] 
            print(f"Landed on {current_property.name}.") 
 
            if current_property.owner is None: 
                print(f"Property available for purchase at ${current_property.purchase_price}.") 
                buy_choice = input("Do you want to buy it? (y/n): ").lower() 
                if buy_choice == 'y': 
                    current_property.buy(player) 
                    print(f"{player.name} bought {current_property.name}.") 
            else: 
                current_property.pay_rent(player) 
                print(f"{player.name} paid ${current_property.rent} rent to {current_property.owner.name}.") 
