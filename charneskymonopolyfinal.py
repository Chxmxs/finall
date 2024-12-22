import json
#USED UMGPT for structure and logic (not copy paste, just initial structure for each)

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
            self.current_space = (self.current_space + steps) % board_size
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
 
#USED UMGPT for buy and rent logic (debug work)
    def buy(self, player): 
        if self.owner is None and player.cash >= self.purchase_price:
            player.cash -= self.purchase_price 
            self.owner = player 
            player.owned_properties.append(self)
            print(f"{player.name} successfully bought {self.name}.")
        elif player.cash < self.purchase_price:
            print(f"{player.name} dosn't have enough cash to buy {self.name}.")
        else:
            print(f"{self.name} is already bought by {self.owner.name}.")
 
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
 
#USED UMGPT for line 68 (debug) dice logic
import random
def roll_dice(): 
    return random.randint(1, 6) + random.randint(1, 6)


def save_game(players):
    with open("monopoly_save.json", "w") as save_file:
        save_data = {
            "players": [
                {
                    "name": player.name,
                    "cash": player.cash,
                    "current_space": player.current_space,
                    "owned_properties": [prop.name for prop in player.owned_properties],
                    "in_jail": player.in_jail
                }
                for player in players
            ]
        }
        json.dump(save_data, save_file)
        print("game was saved successfully")

 #USED UMGPT to debug this i kept getting the variables mixed up
def load_game():
    try:
        with open("monopoly_save.json", "r") as save_file:
            save_data = json.load(save_file)
            players = []
            for pdata in save_data["players"]:
                player = Player(pdata["name"], pdata["cash"])
                player.current_space = pdata["current_space"]
                player.in_jail = pdata["in_jail"]
                player.owned_properties = [
                    next(prop for prop in properties if prop.name == pname)
                    for pname in pdata["owned_properties"]
                ]
                players.append(player)
            return players
    except FileNotFoundError:
        print("no saved game found, starting a new game!")
        return initialize_players()

#USED UMGPT for initializing players 
def initialize_players(): 
    player_count = int(input("How many players? (2-8): "))
    while player_count < 2 or player_count > 8:
        print("Invalid number of players.")
        player_count = int(input("How many players? (2-8): "))
    return [Player(f"Player {i+1}") for i in range(player_count)] 
 
#USED UMGPT for game loop structure (did this whole code by myself and had to re-debug)
def game_loop():
    choice = input("do you want to start game or load one (new/load): ").lower()
    if choice == "load":
        players = load_game()
    else:
        players = initialize_players()

    board_size = len(properties)
    game_over = False 
 
    while not game_over:
        for i, player in enumerate(players):
            if i == 0:
                save_choice = input("do you wanna save the game? (y/n): ").lower()
                if save_choice == "y":
                    save_game(players)

            if player.cash <= 0:
                print(f"{player.name} is out of money and out of the game!")
                players.remove(player)
                continue

            print(f"\n{player.name}'s turn. Cash: ${player.cash}")
            if player.in_jail:
                print(f"{player.name} is in jail. Paying $50 to get out.")
                player.move(0, board_size)  #50 dollars to pay jail, if you cant afford then it wont allow you to pay it and skips ur option to
                continue

            input("Press Enter to roll the diec")
            steps = roll_dice()
            print(f"{player.name} rolled {steps}.")
            player.move(steps, board_size)

            current_property = properties[player.current_space]
            print(f"Landed on {current_property.name}.") 
 
            if current_property.owner is None:
                if player.cash >= current_property.purchase_price:
                    print(f"Property available for purchase at ${current_property.purchase_price}.")
                    buy_choice = input("Do you want to buy it? (y/n): ").lower()
                    if buy_choice == 'y':
                        current_property.buy(player)
                    print(f"{player.name} bought {current_property.name}.")
                else:
                    print(
                        f"You don't have enough cash to buy {current_property.name}. It costs ${current_property.purchase_price}.")
            else: 
                current_property.pay_rent(player) 
                print(f"{player.name} paid ${current_property.rent} rent to {current_property.owner.name}.")

            if player.cash <= 0:
                print(f"{player.name} is bankrupt!") 
                players.remove(player) 
            if len(players) == 1: 
                print(f"{players[0].name} wins the game!") 
                game_over = True 
                break

if __name__ == "__main__":
    print("Welcome to monopoly!")
    game_loop()
