import arcade
import arcade.key
from random import randint
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600



class GameWindow(arcade.Window):
    def __init__(self, width, height):
        self.world = World()
        super().__init__(width, height)
        self.bg = arcade.Sprite('img/bg.png')
        self.attack_s = arcade.Sprite('img/attack_s.png')
        self.block_s = arcade.Sprite('img/block_s.png')
        self.empty_s = arcade.Sprite('img/empty_s.png')
        self.attack = arcade.Sprite('img/attackcard.png')
        self.block = arcade.Sprite('img/blockcard.png')
        self.empty = arcade.Sprite('img/emptycard.png')
        self.bg.set_position(500, 300)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        arcade.draw_text("Your Life : "+str(self.world.life_player),
                         self.width - 320, self.height - 30,
                         arcade.color.WHITE, 15)
        arcade.draw_text("P1's Life : "+str(self.world.life_bot),
                         205, self.height - 30,
                         arcade.color.WHITE, 15)
        
        A = self.world.A
        S = self.world.S
        D = self.world.D
        
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
        if D  == 0:
            self.empty_s.set_position(797,155)
            self.empty_s.draw()
        
        if self.world.game == 1:
            if self.world.B == 1:
                self.block.set_position(300,300)
                self.block.draw()
            if self.world.B == -1:
                self.attack.set_position(300,300)
                self.attack.draw()
            if self.world.B == 0:
                self.empty.set_position(300,300)
                self.empty.draw()

            if self.world.P == 1:
                self.block.set_position(700,300)
                self.block.draw()
            if self.world.P == -1:
                self.attack.set_position(700,300)
                self.attack.draw()
            if self.world.P == 0:
                self.empty.set_position(700,300)
                self.empty.draw()

            arcade.draw_text("Press SPACE to continued",
                         380, 50,
                         arcade.color.WHITE, 15)
            
        if self.world.life_bot == 0:
            arcade.draw_text("YOU WIN",
                         330, 300,
                         arcade.color.WHITE, 50)
        
        if self.world.life_player == 0:
            arcade.draw_text("YOU LOSE",
                         330, 300,
                         arcade.color.WHITE, 50)

                        

class World:
    def __init__(self):
        super().__init__()
        self.A = randint(-1,1)
        self.S = randint(-1,1)
        self.D = randint(-1,1)
        self.B = randint(-1,1)
        self.P = -99
        self.life_bot = 3
        self.life_player = 3
        self.game = 0

    def on_key_press(self, key, key_modifiers):
        if self.game == 0:
            if key == arcade.key.A:
                self.P = self.A
                self.B = randint(-1,1)
                self.fight(self.B,self.P)
                self.A = randint(-1,1)
                self.game = 1
            elif key == arcade.key.S:
                self.P = self.S
                self.B = randint(-1,1)
                self.fight(self.B,self.P)
                self.S = randint(-1,1)
                self.game = 1
            elif key == arcade.key.D:
                self.P = self.D
                self.B = randint(-1,1)
                self.fight(self.B,self.P)
                self.D = randint(-1,1)
                self.game = 1
        if self.game == 1:
            if key == arcade.key.SPACE:
                self.game = 0

    def fight(self,Bot,Player):
        print(Bot)
        print(Player)
        result = Player+Bot
        if result == -1:
            if Player == -1:
                self.life_bot -=1
            else:
                self.life_player -= 1
        


if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()