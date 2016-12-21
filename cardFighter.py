import arcade
import arcade.key
from random import randint
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
a = randint(-1,1)
s = randint(-1,1)
d = randint(-1,1)
b = randint(-1,1)
game = 0


class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
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
        self.world = World()
        self.bg.draw()

        arcade.draw_text("Your Life : "+str(self.world.life_player),
                         self.width - 320, self.height - 30,
                         arcade.color.WHITE, 15)
        arcade.draw_text("Bot's Life : "+str(self.world.life_bot),
                         205, self.height - 30,
                         arcade.color.WHITE, 15)

        if self.world.A == 1:
            self.block_s.set_position(797,455)
            self.block_s.draw()
        if self.world.A == -1:
            self.attack_s.set_position(797,455)
            self.attack_s.draw()
        if self.world.A == 0:
            self.empty_s.set_position(797,455)
            self.empty_s.draw()

        if self.world.S == 1:
            self.block_s.set_position(797,305)
            self.block_s.draw()
        if self.world.S == -1:
            self.attack_s.set_position(797,305)
            self.attack_s.draw()
        if self.world.S == 0:
            self.empty_s.set_position(797,305)
            self.empty_s.draw()

        if self.world.D== 1:
            self.block_s.set_position(797,155)
            self.block_s.draw()
        if self.world.D== -1:
            self.attack_s.set_position(797,155)
            self.attack_s.draw()
        if self.world.D == 0:
            self.empty_s.set_position(797,155)
            self.empty_s.draw()
        
        if game == 1:
            if self.world.B == 1:
                self.block_s.set_position(797,155)
                self.block_s.draw()
            if self.world.B == -1:
                self.attack_s.set_position(797,155)
                self.attack_s.draw()
            if self.world.B == 0:
                self.empty_s.set_position(797,155)
                self.empty_s.draw()
            if self.world.P == 1:
                self.block_s.set_position(797,155)
                self.block_s.draw()
            if self.world.P == -1:
                self.attack_s.set_position(797,155)
                self.attack_s.draw()
            if self.world.P == 0:
                self.empty_s.set_position(797,155)
                self.empty_s.draw()
                        


class World:
    def __init__(self):
        super().__init__()
        self.A = a
        self.S = s
        self.D = d
        self.B = b
        self.P = -99
        self.life_bot = 3
        self.life_player = 3

    def on_key_press(self, key, key_modifiers):
        if game == 0:
            if key == arcade.key.A:
                self.P = self.A
                self.A = randint(-1,1)
                self.game = 1
            elif key == arcade.key.S:
                self.P = self.S
                self.S = randint(-1,1)
                self.game = 1
            elif key == arcade.key.D:
                self.P = self.D
                self.D = randint(-1,1)
                self.game = 1
        if game == 1:
            if key == arcade.key.SPACE:
                self.game = 0

    def fight(Bot,Player):
        result = Bot-Player
        if result == 1:
            self.life_bot -= 1
            self.B = randint(-1,1)
        if result == -1:
            self.life_player -= 1
            self.B = randint(-1,1)
        if result == 0:
            self.B = randint(-1,1)


if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()