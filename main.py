"""
Sprite Collect Coins

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_collect_coins
"""

import random
from fileinput import filename

import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50
BARRIER_COUNT = 20
LIFE_COUNT = 3

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Sprite Collect Coins Example"


class MyGame(arcade.Window):
        """ Our custom Window Class"""

        def __init__(self):
            """ Initializer """
            # Call the parent class initializer
            super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

            # Variables that will hold sprite lists
            self.player_list = None
            self.coin_list = None
            self.barrier_list = None
            self.life_list = None

            # Set up the player info
            self.player_sprite = None
            self.score = 0

            # Don't show the mouse cursor
            self.set_mouse_visible(False)

            arcade.set_background_color(arcade.color.AMAZON)

        def setup(self):
            """ Set up the game and initialize the variables. """

            # Sprite lists
            self.player_list = arcade.SpriteList()
            self.coin_list = arcade.SpriteList()
            self.barrier_list = arcade.SpriteList()
            self.life_list = arcade.SpriteList()
            # Score
            self.score = 0
            self.lives = 3
            # Set up the player
            # Character image from kenney.nl
            img = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
            self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
            self.player_sprite.center_x = 50
            self.player_sprite.center_y = 50
            self.player_list.append(self.player_sprite)

            # Create the coins
            for i in range(COIN_COUNT):

                # Create the coin instance
                # Coin image from kenney.nl
                coin = arcade.Sprite(":resources:images/items/coinGold.png",
                                     SPRITE_SCALING_COIN)

                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # Add the coin to the lists
                self.coin_list.append(coin)
            for i in range(BARRIER_COUNT):
                barrier = arcade.Sprite("imagenes/cuadrado.png",
                                        SPRITE_SCALING_COIN)
                barrier.center_x = random.randrange(SCREEN_WIDTH)
                barrier.center_y = random.randrange(SCREEN_HEIGHT)

                self.barrier_list.append(barrier)

            for i in range(LIFE_COUNT):
                live = arcade.Sprite("imagenes/corazon.png",
                                        SPRITE_SCALING_COIN*10)
                live.center_x = random.randrange(SCREEN_WIDTH)
                live.center_y = random.randrange(SCREEN_HEIGHT)

                self.life_list.append(live)
        def on_draw(self):
            """ Draw everything """
            self.clear()
            self.coin_list.draw()
            self.barrier_list.draw()
            self.life_list.draw()
            self.player_list.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(text=output, start_x=10, start_y=20,
                             color=arcade.color.WHITE, font_size=14)
            lives = f"lives: {self.lives}"
            arcade.draw_text(text=lives, start_x=10, start_y=40,
                             color=arcade.color.WHITE, font_size=14)
        def on_mouse_motion(self, x, y, dx, dy):
            """ Handle Mouse Motion """

            # Move the center of the player sprite to match the mouse x, y
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

        def on_update(self, delta_time):
            """ Movement and game logic """

            # Generate a list of all sprites that collided with the player.
            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                  self.coin_list)
            barrier_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                    self.barrier_list)
            life_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.life_list)
            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
            for barrier in barrier_hit_list:
                barrier.remove_from_sprite_lists()
                self.lives -= 1
            for live in life_hit_list:
                live.remove_from_sprite_lists()
                self.lives = 3
def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
