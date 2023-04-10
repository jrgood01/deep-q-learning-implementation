# PongGym.py

## Code Summary

This Python file contains the implementation of the `PongGym` class, which is a subclass of the `Gym` class from the `RLGym` module. The `PongGym` class represents a simplified version of the game of Pong, where two paddles move up and down to prevent a ball from reaching the edges of the screen. The class defines methods to update the position of the ball and paddles, detect collisions, and apply actions chosen by a reinforcement learning algorithm.

## Class Summaries

### Paddle

This class represents a paddle in the game of Pong. It has instance variables for the paddle's position, width, and height. It has two methods:

- `drawPaddle(self, curState)`: This method takes a numpy array `curState` representing the current state of the game and modifies it to draw the paddle at its current position.
- `detectHit(self, x, y, w, h)`: This method takes four arguments representing the position and size of a rectangular area and returns a Boolean value indicating whether the area overlaps with the paddle.

### Ball

This class represents a ball in the game of Pong. It has instance variables for the ball's position and velocity. It has one method:

- `drawBall(self, curState)`: This method takes a numpy array `curState` representing the current state of the game and modifies it to draw the ball at its current position.

### PongGym

This class represents the game of Pong itself. It is a subclass of the `Gym` class from the `RLGym` module. It has instance variables for the width and height of the game screen, as well as instances of the `Paddle` and `Ball` classes. It has methods to update the game state, apply actions, and reset the game. 

## Method Summaries

### PongGym.__init__()

```
def __init__(self, width, height):
```

This method initializes an instance of the Pong game. It takes in two parameters `width` and `height` to determine the size of the game screen. It initializes instances of the `Paddle` and `Ball` classes as instance variables. It also calls the `__init__()` method of the parent class (`Gym`) with the given width, height, and 9 as parameters.

### PongGym.paddleRUp()

```
def paddleRUp(self):
```

This method moves the right paddle upwards by 3 pixels if doing so will keep the paddle within the game screen height. It takes no parameters and returns nothing.

### PongGym.paddleRDown()

```
def paddleRDown(self):
```

This method moves the right paddle downwards by 3 pixels if doing so will keep the paddle within the game screen height. It takes no parameters and returns nothing.

### PongGym.paddleLUp()

```
def paddleLUp(self):
```

This method moves the left paddle upwards by 3 pixels if doing so will keep the paddle within the game screen height. It takes no parameters and returns nothing.

### PongGym.paddleLDown()

```
def paddleLDown(self):
```

This method moves the left paddle downwards by 3 pixels if doing so will keep the paddle within the game screen height. It takes no parameters and returns nothing.

### PongGym.applyAction(action)

```
def applyAction(self, action):
```

This method takes an integer `action` representing a move to be made by the paddles in the game. It updates the position of the paddles according to the specified action and returns the updated game state.

### PongGym.update()

```
def update(self):
```

This method updates the position of the ball and detects collisions with the paddles or edges of the game screen. It also calls the `drawPaddle()` and `drawBall()` methods of the paddle and ball instances to update the game state.

### PongGym.reset()

```
def reset(self):
```

This method resets the game by randomizing the positions and velocities of the ball and paddles.

## Example Usage

```python
# Create an instance of the PongGym class with a game screen size of 250x250.
game = PongGym(250, 250)

# Apply an action to move the left paddle up.
reward = game.applyAction(1)

# Get the current state of the game.
state = game.getState()

# Reset the game.
game.reset()
```