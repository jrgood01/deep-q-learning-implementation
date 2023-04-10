# RLGym.py

A Python file containing a class called **Gym** which is used to create environments for reinforcement learning agents. 

## Class Summaries

### Gym

- **Description**: The gym class initializes the environment for the agent and provides functionality to update the game state, clear the state, and render the game. This class contains an abstract method, *applyAction*, which is meant to be overriden by subclasses to dictate the behavior of the game. 
- **Properties**: 
    - *self.width*: an integer representing the width of the game screen
    - *self.height*: an integer representing the height of the game screen
    - *self.action_set_size*: an integer representing the size of the action set
    - *self.state*: a numpy array representing the current state of the game
    - *self.agent*: an instance of a DeepQAgent object that serves as the agent for the game
  - **Methods**:
    - *clear_state(self)*: clears the state of the game by setting it to an array of zeros
    - *updateState(self, training=True)*: updates the game state by applying the best action according to the agent's model. The method takes in a boolean training flag, which when set to True, enables the agent to learn from the state transitions. This method returns nothing.
    - *render(self)*: displays the current state of the game on the screen.
    - *applyAction(self, action)*: an abstract method that is meant to be overriden by subclasses to control the behavior of the game based on the given action. This method takes in an action and returns nothing.

## Method Summaries

### applyAction

- **Description**: This method is an abstract method that is meant to be overriden by subclasses to control the behavior of the game based on the given action. This method takes in an action and returns nothing.
- **Parameters**: 
    - *action*: an integer representing the action to be taken in the game.
- **Example Usage**: This method should be overridden by a subclass and can have implementation as follows. 

```
def applyAction(self, action):
    if action == 0:
        self.paddleLUp()
    elif action == 1:
        self.paddleLDown()
    elif action == 2:
        self.paddleRUp()
    elif action == 3:
        self.paddleRDown()
    ...
```

### updateState

- **Description**: Updated the state of the game by applying the best action according to the agent's model using PyTorch to determine the best action to be taken based on the previous state. The method takes in a boolean training flag, which when set to True, enables the agent to learn from the state transitions.
- **Parameters**: 
    - *training*: a boolean flag that when set to True allows the agent to learn from the state transitions made in the game.
- **Example Usage**: 

```
Gym_Instance.updateState(training=True)
```

### clear_state

- **Description**: Method to recall the initialization and reset the attributes of the instance. This method takes no parameters and returns nothing.
- **Parameters**: N/A
- **Example Usage**: 

```
Gym_Instance.clear_state()
```

### render

- **Description**: Update the rendered state of the game on the screen
- **Parameters**: N/A
- **Example Usage**: 

```
Gym_Instance.render()
```

## Example Usage

Example usage of the methods defined in Gym class in a training loop could be as follows:

```
Gym_Instance = Gym(600, 400, 8)
training = True
for i in range(500):
    Gym_Instance.updateState(training=training)
    if training:
        if i % 5 == 0:
            Gym_Instance.render()
        if i % 10 == 0:
            Gym_Instance.agent.updateModel()
```

In the above example, we create an instance of the Gym class with a screen of size 600x400 and 8 possible actions. We set the training flag to True and then run a loop for 500 training iterations. In each iteration, we call the *updateState* method of the Gym instance which applies the best action to the game state, updates the agent's model and returns no output. We also call the *render* method every 5th iteration to visualize the progress of the game. We also update the agent's model every 10th iteration.