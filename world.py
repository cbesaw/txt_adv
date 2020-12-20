import random
import enemies


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
        
        Before you are two alleyways to the north and east. A door to the city 
        guard/'s quarter lies ajar to your west. 
        
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
            self.dead_text = "The remains of the townsperson lies "\
                             "motionless on the ground."
        else:
            self.enemy = enemies.Zombie2()
            self.alive_text = "A zombified guardsman staggers "\
                              "towards you."
            self.dead_text = "The remains of the guardsman lies "\
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
            
        

world_map = [
    [None, VictoryTile(1,0), None],
    [None, EncounterTile(1,1), None],
    [BoringTile(0,2), StartTile(1,2), EncounterTile(2,2)],
    [None, BoringTile(1,3), None]
    ]


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
    
    
    
    


