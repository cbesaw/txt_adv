from player import Player
        


def play():
    print("Journey into the City of the Dead")
    player = Player()
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North!")
        elif action_input in ['s', 'S']:
            print("Go South!")
        elif action_input in ['e', 'E']:
            print("Go East!")
        elif action_input in ['w', 'W']:
            print("Go West!")
        elif action_input in ['i', 'I']:
            player.print_inventory()
        else:
            print("Invalid Action!")
        
        
def get_player_command():
    return input('Action: ')



play()
    
    



    