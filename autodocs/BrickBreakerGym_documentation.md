# BrickBreakerGym.py Documentation

## Code Summary

The `BrickBreakerGym.py` file contains a Python class `BrickBreakerGym` which represents a simple Brick Breaker game. The class creates a canvas and adds bricks, paddle, and a ball. The user can control the paddle to hit the ball against the bricks and earn rewards.

## Class Summaries

### `Brick`

This class represents a brick that will be present on the canvas in the Brick Breaker game. It has the following methods:

#### `__init__(self, x, y, width, height, lives=5)`

This method initializes the brick with the given x-coordinate, y-coordinate, width, height, and lives.

#### `isOverlapping(self, x, y, width, height)`

This method checks if the given coordinates and dimensions overlap with the brick it is called upon. It returns True if they overlap, and False otherwise.

#### `getColor(self)`

This method returns a list of three integers - [0, 0, 0], i.e., black.

### `BrickBreakerGym`

This class represents a Brick Breaker game. It has the following methods:

#### `__init__(self, res_x, res_y, y_fill_proportion=.5, brick_inlay_proportion=.3, brick_width=100, brick_height=20)`

This method initializes the Brick Breaker game with the given parameters. It creates a canvas and adds bricks, paddle, and a ball to the canvas.

#### `startRender(self)`

This method displays the canvas.

#### `detectBrickHit(self)`

This method checks for the collision or overlapping of the ball with each of the bricks. If the ball overlaps with any brick, it reduces the number of lives of that brick by 1, increases the reward, changes the direction of the ball, and returns True. If no collision is detected, it returns False.

#### `flip(self)`

This method updates the canvas by redrawing the bricks, paddle, and ball at their updated positions. It also checks if the ball has hit the paddle or any of the bricks and updates the game accordingly.

#### `paddle_right(self)`

This method moves the paddle to the right by 2 units.

#### `paddle_left(self)`

This method moves the paddle to the left by 2 units.

#### `on_keyboard_event(self, key, shift_key, ctrl_key, meta_key)`

This method is called when a keyboard event is triggered. It moves the paddle to the left by 5 units.

## Method Summaries

### `Brick.isOverlapping`

```python
def isOverlapping(self, x, y, width, height):
    """
    Check if the given coordinates and dimensions overlap with the brick.
    
    Parameters:
    x (float) : The x-coordinate of the given object.
    y (float) : The y-coordinate of the given object.
    width (float) : The width of the given object.
    height (float) : The height of the given object.
    
    Returns:
    bool : True if the given object overlaps with the brick, False otherwise.
    """
```

### `BrickBreakerGym.__init__`

```python
def __init__(self, res_x, res_y, y_fill_proportion=.5, brick_inlay_proportion=.3, brick_width=100, brick_height=20):
    """
    Initialize the Brick Breaker game with the given parameters.
    
    Parameters:
    res_x (int) : The width of the canvas.
    res_y (int) : The height of the canvas.
    y_fill_proportion (float) : The portion of the canvas that will be filled with bricks (default = .5).
    brick_inlay_proportion (float) : The portion of the area filled by bricks that will be filled with a brick (default = .3).
    brick_width (int) : The width of each brick (default = 100).
    brick_height (int) : The height of each brick (default = 20).
    """
```

### `BrickBreakerGym.startRender`

```python
def startRender(self):
    """
    Display the canvas.
    """
```

### `BrickBreakerGym.detectBrickHit`

```python
def detectBrickHit(self):
    """
    Check for the collision or overlapping of the ball with each of the bricks.
    If the ball overlaps with any brick,
    it reduces the number of lives of that brick by 1,
    increases the reward,
    changes the direction of the ball,
    and returns True.
    If no collision is detected, it returns False.
    """
```

### `BrickBreakerGym.flip`

```python
def flip(self):
    """
    Update the canvas by redrawing the bricks, paddle, and ball at their updated positions.
    It also checks if the ball has hit the paddle or any of the bricks and updates the game accordingly.
    """
```

### `BrickBreakerGym.paddle_right`

```python
def paddle_right(self):
    """
    Move the paddle to the right by 2 units.
    """
```

### `BrickBreakerGym.paddle_left`

```python
def paddle_left(self):
    """
    Move the paddle to the left by 2 units.
    """
```

### `BrickBreakerGym.on_keyboard_event`

```python
def on_keyboard_event(self, key, shift_key, ctrl_key, meta_key):
    """
    Called when a keyboard event is triggered.
    Move the paddle to the left by 5 units.
    """
```

## Example Usage

```python
brickBreaker = BrickBreakerGym(800, 600) # Initialize a brick breaker game with width=800px and height=600px.
brickBreaker.startRender() # Display the canvas.
while True:
    brickBreaker.flip() # Update the canvas.
```