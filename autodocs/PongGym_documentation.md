# Code Summary

The `PongGym.py` file contains a Python class `PongGym` which is a subclass of `Gym` class from the RLGym package. The class simulates a Pong game environment where agents can take actions and receive rewards based on the outcomes. The game board includes two paddles and a ball, which can move within certain constraints.

It contains four methods to update the game environment: `update()`, `applyAction()`, `reset()`, and some additional paddle control methods. 

# Class Summaries

## Paddle class
The `Paddle` class contains the following attributes:
- `x`: x-coordinate of the upper-left point of the paddle
- `y`: y-coordinate of the upper-left point of the paddle
- `w`: width of the paddle
- `h`: height of the paddle

The class contains two additional methods:
- `drawPaddle(curState)`: updates the current state of the game with the paddle
- `detectHit(x, y, w, h)`: detects if the ball is in contact with the paddle

## Ball class
The `Ball` class contains the following attributes:
- `x`: x-coordinate of the upper-left point of the ball
- `y`: y-coordinate of the upper-left point of the ball
- `dx`: movement distance on the x-axis
- `dy`: movement distance on the y-axis

The class contains one additional method:
- `drawBall(curState)`: updates the current state of the game with the ball

## PongGym class
The `PongGym` class is a subclass of the `Gym` class which uses the following attributes:
- `paddleL`: instance of the `Paddle` class for the left paddle
- `paddleR`: instance of the `Paddle` class for the right paddle
- `ball`: instance of the `Ball` class
- `height`: game screen height
- `width`: game screen width

The class contains the following methods:
- `__init__(self, width, height)`: initializes the game board
- `paddleRUp(self)`: moves the right paddle upwards
- `paddleRDown(self)`: moves the right paddle downwards
- `paddleLUp(self)`: moves the left paddle upwards
- `paddleLDown(self)`: moves the left paddle downwards
- `applyAction(self, action)`: applies the specified action to update the paddle positions and ball movement
- `update(self)`: updates the game state and returns the reward depending on the ball and paddle position
- `reset(self)`: resets the game board to its initial state

# Method Summaries

## Paddle.drawPaddle(curState)
Draws the current paddle state on the game screen. 

### Parameters
- `curState`: current state of the game

### Output
- None

## Paddle.detectHit(x, y, w, h)
Returns true if the rectangle with given properties collides with the paddle object.

### Parameters
- `x`: x-coordinate of the object
- `y`: y-coordinate of the object
- `w`: width of the object
- `h`: height of the object

### Output
- bool: True if the paddle is hit, False otherwise

## Ball.drawBall(curState)
Draws the ball on the game screen.

### Parameters
- `curState`: current state of the game

### Output
- None

## PongGym.__init__(self, width, height)
Initializes the game board with paddles and ball.

### Parameters
- `width`: screen width
- `height`: screen height

### Output
- None

## PongGym.paddleRUp(self)
Moves the right paddle up by a fixed distance of 3 units if the new position is within the game screen.

### Parameters
- None

### Output
- None

## PongGym.paddleRDown(self)
Moves the right paddle down by a fixed distance of 3 units if the new position is within the game screen.

### Parameters
- None

### Output
- None

## PongGym.paddleLUp(self)
Moves the left paddle up by a fixed distance of 3 units if the new position is within the game screen.

### Parameters
- None

### Output
- None

## PongGym.paddleLDown(self)
Moves the left paddle down by a fixed distance of 3 units if the new position is within the game screen.

### Parameters
- None

### Output
- None

## PongGym.applyAction(self, action)
Applies the action and updates the game state accordingly.

### Parameters
- `action`: action to be taken on the game environment, an integer value between 0 and 7

### Output
- int: returns the reward value based on the current state of the game

## PongGym.update(self)
Updates the game environment based on the ball and paddle positions.

### Parameters
- None

### Output
- int: returns the reward value based on the current state of the game

## PongGym.reset(self)
Resets