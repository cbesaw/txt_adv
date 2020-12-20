import items
import world

class Player:
    def __init__(self):
        self.inventory = [items.Dagger(),
                          items.Longsword(),
                          items.HolySymbol(),
                          'Gold(5)',
                          'Bread']
        
        self.x = 1
        self.y = 2
        self.hp = 100
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def move_north(self):
        self.move(dx=0, dy=-1)
    
    def move_south(self):
        self.move(dx=0, dy=1)
        
    def move_east(self):
        self.move(dx=1, dy=0)
        
    def move_west(self):
        self.move(dx=-1, dy=0)
        
    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
            
        return(best_weapon)
    
    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use your {} against the {} for {} damage".format(best_weapon.name,
                                                       enemy.name,
                                                       best_weapon.damage))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed the {}!".format(enemy.name))
        else:
            print("The {} still stands before you".format(enemy.name))
            
        
        
        
        
        