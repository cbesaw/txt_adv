from player import Player
import world
from collections import OrderedDict
        


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory,
                     "Print inventory")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")        
    if isinstance(room, world.EncounterTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
    if player.hp < 25:
        action_adder(actions, 'h', player.heal, "Heal")
        
    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))
    
    
def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")




def play():
    print("""
        After five days of traveling you arrive in the abandoned city of 
        Norbrook. You are here to look for your Lord, who disappeared after
        traveling to the city over two months ago. Norbrook has been abandoned
        for over a hundred years, but hushed whispers spread rumors of sound
        and shadow coming from the once bustling city. 
        
        Your Lord never told you why he came to this place, but the head cleric
        of your order has tasked you with finding information about his
        whereabouts.
        
        You feel nervous. Your training had only just begun as a paladin of
        the order when your lord disappeared. Shadows and light dance in your
        periphery. It is hard to tell if there is movement or whether your
        tired eyes are playing tricks on you. 
        
        You stand in an intersection after entering the city gate. The city,
        while abandoned, surprisingly does not look ruinous. 
          """)
    world.parse_world_dsl()
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        choose_action(room, player)
        room.modify_player(player)

        

play()
    
    



    