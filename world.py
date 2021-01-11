import random
import enemies
import sys
import npc


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")
        
    def modify_player(self, player):
        pass
        
        
class StartTile(MapTile):
    def intro_text(self):
        return """
        Before you are two alleyways to the north and east. A door to a city 
        guard's post lies ajar to your west. 
        
        You may also abandon your mission by leaving through the gate behind
        you to the south.
        """
        
class BoringTile(MapTile):
    def intro_text(self):
        return """
        This is a placeholder empty tile.
        """
        
class VictoryTile(MapTile):
    def intro_text(self):
        return """
        This is a placeholder victory tile.
        """

class EncounterTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r <= 0.80:
            self.enemy = enemies.Zombie()
            self.alive_text = "A zombified townsperson staggers "\
                              "towards you."
            self.dead_text = "The remains of the townsperson lie "\
                             "motionless on the ground."
        else:
            self.enemy = enemies.Zombie2()
            self.alive_text = "A zombified guardsman staggers "\
                              "towards you."
            self.dead_text = "The remains of the guardsman lie "\
                             "motionless on the ground."
            
        super().__init__(x, y)
        
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
    
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("The {} attacks you for {} damage.".format(self.enemy.name,
                                                             self.enemy.damage))
 
            
class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)
        

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name,
                                        item.value))
            while True:
                user_input = input("Choose an item or press Q to exit: ")
                if user_input in ['Q', 'q']:
                    return
                else:
                    try:
                        choice = int(user_input)
                        to_swap = seller.inventory[choice - 1]
                        self.swap(seller, buyer, to_swap)
                    except ValueError:
                        print("Invalid choice!")
                        
                        
    def swap(self,  seller, buyer, item):
        if item.value > buyer.gold:
            print("You don't have enough gold.")
            return 
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("You bought a {} for {} gold.".format(item.name,
                                                    item.value))
        
    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("What'a buyin? ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("What'a sellin? ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")
                
    def intro_text(self):
        return """
        A frail hooded humanoid sits in the middle of a dilapidated house. The figure 
        greets you with a toothy smile and offers to trade items for gold.
        """
        
class GuardPostTile1(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 25)
        self.gold_claimed = False
        super().__init__(x, y)
        
    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            print("You found {} gold!".format(self.gold))
            player.gold = player.gold + self.gold
                      
    def intro_text(self):
        if self.gold_claimed:
            return """
            The guard post stands eerily empty. You feel the urge to move on.
            """
        else:
            return """
            You find an abandoned guard house. Hastily abandoned, the previous
            occupant left their gold and belongings on the table. You pick them up.
            """
            
        
            
            
class EndingTile1(MapTile):
    def intro_text(self):
        return """
    A sense of dread overwhelms you. Your body and mind in sync tell you to flee...
    
    You ride hard away from Norbrook. Every mile between you and that cursed place serves
    as a reminder of your cowardice. 
    """
 
    
#Map Building
    
world_dsl = """
| |VT| | |
| |ET| | |
|GP1|ST|ET|TT|
| |EN1| | |
"""
            
 
def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
        
    return True

tile_type_dict = {"VT": VictoryTile,
                  "ET": EncounterTile,
                  "ST": StartTile,
                  "EN1": EndingTile1,
                  "GP1": GuardPostTile1,
                  "TT": TraderTile,
                  " ": None}

start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
        
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)
            
        world_map.append(row)


world_map = []


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
    
    
    
    


