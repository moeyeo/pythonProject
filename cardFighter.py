import arcade
import arcade.key
from random import randint
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
A = randint(-1,1)
S = randint(-1,1)
D = randint(-1,1)

 
class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)
        self.bg = arcade.Sprite('img/bg.png')
        self.attack_s = arcade.Sprite('img/attack_s.png')
        self.block_s = arcade.Sprite('img/block_s.png')
        self.empty_s = arcade.Sprite('img/empty_s.png')
        self.bg.set_position(500, 300)

    def on_draw(self):
        arcade.start_render()
        self.world = World()
        self.bg.draw()
        if A == 1:
            self.block_s.set_position(797,455)
            self.block_s.draw()
        if A == -1:
            self.attack_s.set_position(797,455)
            self.attack_s.draw()
        if A == 0:
            self.empty_s.set_position(797,455)
            self.empty_s.draw()

        if S == 1:
            self.block_s.set_position(797,305)
            self.block_s.draw()
        if S == -1:
            self.attack_s.set_position(797,305)
            self.attack_s.draw()
        if S == 0:
            self.empty_s.set_position(797,305)
            self.empty_s.draw()

        if D == 1:
            self.block_s.set_position(797,155)
            self.block_s.draw()
        if D == -1:
            self.attack_s.set_position(797,155)
            self.attack_s.draw()
        if D == 0:
            self.empty_s.set_position(797,155)
            self.empty_s.draw()
        
                    
 
class World:
    def __init__(self):
        super().__init__()
        life_bot = 3
        life_player = 3
        game = 0

    def on_key_press(self, key, key_modifiers):
        if game == 0:
            if key == arcade.key.A:
                A = randint(-1,1)
            elif key == arcade.key.S:
                S = randint(-1,1)
            elif key == arcade.key.D:
                D = randint(-1,1)
            game = 1
        if game == 1:
            if key == arcade.key.SPACE:
                game = 0

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()