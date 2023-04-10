# RLGym.py Documentation

## Code Summary
This file contains the implementation of the `Gym` class which serves as a base class for creating custom environments for training and evaluating reinforcement learning agents.

The `Gym` class accepts the following parameters:
- `width` - an integer representing the width of the environment (in pixels)
- `height` - an integer representing the height of the environment (in pixels)
- `action_set_size` - an integer representing the size of the action set
- `render` - a boolean indicating whether to render the environment

The `Gym` class contains the following methods:
- `clear_state`: This method clears the state of the environment.
- `applyAction`: An abstract method that takes an action as input and updates the position of game paddles accordingly.
- `updateState`: This method updates the state of the environment based on the input action.
- `render`: This method renders the environment.

## Class Summaries
N/A

## Method Summaries
### Gym.clear_state()
This method clears the state of the environment. 

#### Example Usage
```python
env = Gym(200, 200, 10)
env.clear_state()
```

### Gym.applyAction(action)
This is an abstract method that takes an action as input and updates the position of game paddles accordingly. The method has eight different actions that perform various actions related to paddle movement. These actions call submethods 'paddleLDown', 'paddleRDown', 'paddleLUp', and 'paddleRUp' with different configurations of arguments. These methods move the paddle up or down based on their current position and the game window limits. The 'applyAction' method returns the output of the 'update' method. 
This method is an abstract method that takes in a parameter called 'action'. It does not have any implementation details within it and serves as a placeholder for subclasses to implement. Therefore, the output and the inner workings of the 'applyAction' method are dependent on the implementation details of its subclasses. 

### Gym.updateState(training=True)
This method updates the state of the environment based on the input action. If the length of 'state_history' is greater than or equal to 'max_buffer_len', the method first checks if 'training' is set to True. If so, it calls the 'updateWeights' method. The 'state_history', 'action_history', 'reward_history', and 'inference_history' lists are then reset. If 'training' is set to True, the method appends the new 'state', 'action', and 'reward' to their respective lists. The output of this method is void as it updates the state of the object as per the input parameters.

#### Example Usage
```python
env = Gym(200, 200, 10)
env.updateState()
```

### Gym.render()
This method renders the environment.

#### Example Usage
```python
env = Gym(200, 200, 10)
env.render()
```

## Example Usage 
```python
import numpy as np
import torch
import DeepQAgent
import tkinter as tk
from abc import abstractmethod
from PIL import Image, ImageTk
import time
import cv2
import matplotlib.pyplot as plt
import IPython.display
import PIL.Image
import random

class CustomEnv(Gym):
    def __init__(self, width, height, action_set_size, render=True):
        super().__init__(width, height, action_set_size, render)
        
    def applyAction(self, action):
        # custom implementation of applyAction
        pass

env = CustomEnv(200, 200, 10)
env.clear_state()

for i in range(10):
    env.updateState(training=True)
    env.render()
```