import random
import enemies
import sys


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
            
class EndingTile1(MapTile):
    def intro_text(self):
        return """
    A sense of dread overwhelms you. Your body and mind in sync tell you to flee...
    
    You ride hard away from Norbrook. Every mile between you and that cursed place serves
    as a reminder of your cowardice. 
    """
 
world_dsl = """
| |VT| |
| |ET| |
|ET|ST|ET|
| |EN1| |
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
                  " ": None}

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
    
    
    
    


