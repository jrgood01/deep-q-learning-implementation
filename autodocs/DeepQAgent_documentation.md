# DeepQAgent.py

This Python module contains the implementation of the `Agent` class, which is a deep learning agent trained using the Q-learning algorithm. 

## Code Summary

The `Agent` class has the following attributes:

- `model`: an instance of the `DeepQNet.Net` class that represents the deep neural network used to model the Q function.
- `criterion`: an instance of the `torch.nn.MSELoss` class used to calculate the mean squared error loss between the predicted Q values and the target Q values during training.
- `optimizer`: an instance of the `torch.optim.Adam` class used to optimize the parameters of the `model` using stochastic gradient descent.

- `state_history`: a list of the history of states visited by the agent.
- `action_history`: a list of the history of actions taken by the agent.
- `reward_history`: a list of the history of rewards received by the agent.
- `inference_history`: a list of the history of Q value predictions made by the agent.

- `max_buffer_len`: an integer representing the maximum length of the history buffers for states, actions, rewards, and Q value predictions.
- `model_update_horizon`: an integer representing the number of steps the agent takes before updating the `model`.
- `alpha`: a float representing the learning rate used when updating the Q values.
- `discount_factor`: a float representing the discount factor used to scale the estimated future rewards in the Q value update.
- `epsilon_greedy`: a float representing the exploration rate of the agent used during action selection.

The `Agent` class has the following methods:

### __init__(self, input_width, input_height, action_set_size, model_update_horizon=20, discount_factor=.8, alpha=.8, epsilon_greedy=.1)

This method initializes a new instance of the `Agent` class.

#### Args:
- `input_width`: an integer representing the width of the input image.
- `input_height`: an integer representing the height of the input image.
- `action_set_size`: an integer representing the number of possible actions that the agent can take.
- `model_update_horizon`: an integer representing the number of steps the agent takes before updating the `model`. Default is 20.
- `discount_factor`: a float representing the discount factor used to scale the estimated future rewards in the Q value update. Default is .8.
- `alpha`: a float representing the learning rate used when updating the Q values. Default is .8.
- `epsilon_greedy`: a float representing the exploration rate of the agent used during action selection. Default is .1.

### determineAction(self, state, epsilon_greedy=True)

This method determines the action that the agent takes based on the input state and the Q values predicted by the `model`.

#### Args:
- `state`: a 2-D numpy array representing the current state of the agent.
- `epsilon_greedy`: a boolean representing whether to use an epsilon-greedy strategy when selecting an action. Default is `True`.

### apply(self, state, action, reward, training=True)

This method applies the specified action to the given state and updates the history buffers for the agent's states, actions, and rewards.

#### Args:
- `state`: a 2-D numpy array representing the current state of the agent.
- `action`: an integer representing the action to be taken by the agent.
- `reward`: a float representing the reward received by the agent after taking the specified action.
- `training`: a boolean representing whether the agent is currently training. Default is `True`.

### calculateBellmanUpdateValue(self, loc, action)

This method calculates the value of the Bellman update for a specific pair of state and action.

#### Args:
- `loc`: an integer representing the index of the current state in the `state_history` buffer.
- `action`: an integer representing the index of the current action in the `action_history` buffer.

### updateWeights(self)

This method updates the weights of the `model` based on the Q values stored in the history buffers.

## Example Usage

```
import DeepQAgent

agent = DeepQAgent.Agent(input_width=128, input_height=128, action_set_size=4)
state = np.ones((128, 128))
action = agent.determineAction(state)
reward = 1.0
agent.apply(state, action, reward)

for i in range(100):
    state = np.ones((128, 128))
    action = agent.determineAction(state)
    reward = 1.0
    agent.apply(state, action, reward)

agent.updateWeights()
```