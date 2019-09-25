"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade

SCREEN_WIDTH = 640  
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Keyboard Example"
MOVEMENT_SPEED = 3


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x  #allows you to control the position of the ball on the X plane
        self.position_y = position_y #allows you to control the position of the ball on the Y plane
        self.change_x = change_x  #allows you to directly change the ball's position on the x axis
        self.change_y = change_y #allows you to directly change the ball's position on the y axis
        self.radius = radius 
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius: #if the X value is lower than the set radius of the screen, it will automatically stop once it reaches the set value
            self.position_x = self.radius 

        if self.position_x > SCREEN_WIDTH - self.radius: #if the X value is larger than the set radius, it will automatically stop
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius: #if the Y value is larger than the set height of the screen it will stop once it reaches the top.
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) #Pretty self explanatory, sets the background color of the window as grey.

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render() #opens python arcade
        self.ball.draw() #draws the ball in python arcade 

    def update(self, delta_time): #updates the current location of the ball
        self.ball.update() 

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT: #moves to ball to the left when the left arrow key is pressed
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT: #moves the ball right when the right airrow key is pressed
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP: #moves the ball up when the up arrow key is pressed
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN: #moves the ball down when the arrow key is pressed down
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT: #stops the ball when the left or right arrow keys are released
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN: #stops the ball from moving up and down when the up or down arrow keys are released
            self.ball.change_y = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  #Opens the window of the game.
    arcade.run() #Nothing starts without this


if __name__ == "__main__":
    main()