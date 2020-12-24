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



world_dsl = """
| |VT| |
| |ET| |
|BT|ST|ET|
| |EN1| |
"""
        

world_map = [
    [None, VictoryTile(1,0), None],
    [None, EncounterTile(1,1), None],
    [BoringTile(0,2), StartTile(1,2), EncounterTile(2,2)],
    [None, EndingTile1(1,3), None]
    ]


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
    
    
    
    


