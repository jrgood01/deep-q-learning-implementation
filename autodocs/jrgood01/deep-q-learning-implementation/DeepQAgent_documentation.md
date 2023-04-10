# DeepQAgent Documentation

## Code Summary

The `DeepQAgent` class is a reinforcement learning agent that utilizes a deep Q-network for making decisions. It has several methods that enable it to update its Q-values and make decisions based on the state of the system.

The class takes the following parameters:

- `input_width` (integer): The width of the input image.
- `input_height` (integer): The height of the input image.
- `action_set_size` (integer): The number of actions available to the agent.
- `model_update_horizon` (integer): The frequency at which the agent updates its model.
- `discount_factor` (float): The discount rate for future rewards.
- `alpha` (float): The learning rate.
- `epsilon_greedy` (float): The probability of selecting a random action as opposed to the best action.

The class has the following methods:

- `__init__(self, input_width, input_height, action_set_size, model_update_horizon=20, discount_factor=.8, alpha=.8, epsilon_greedy=.1)`: Constructor method that initializes the agent.
- `determineAction(self, state, epsilon_greedy=True)`: Determines the action the agent should take given its current state.
- `apply(self, state, action, reward, training=True)`: Applies a given action to the agent and updates its state and reward history.
- `calculateBellmanUpdateValue(self, loc, action)`: Calculates the Bellman update for a given state-action pair.
- `updateWeights(self)`: Updates the Q-network weights based on the agent's experiences.

## Method Summaries

### __init__(self, input_width, input_height, action_set_size, model_update_horizon=20, discount_factor=.8, alpha=.8, epsilon_greedy=.1)

Constructor method that initializes the agent.

**Parameters:**

- `input_width` (integer): The width of the input image.
- `input_height` (integer): The height of the input image.
- `action_set_size` (integer): The number of actions available to the agent.
- `model_update_horizon` (integer): The frequency at which the agent updates its model.
- `discount_factor` (float): The discount rate for future rewards.
- `alpha` (float): The learning rate.
- `epsilon_greedy` (float): The probability of selecting a random action as opposed to the best action.

### determineAction(self, state, epsilon_greedy=True)

Determines the action the agent should take given its current state.

**Parameters:**

- `state` (numpy array): The current state of the agent.
- `epsilon_greedy` (bool): Whether or not the agent should use epsilon-greedy selection.

**Returns:**

- The action that the agent should take.

### apply(self, state, action, reward, training=True)

Applies a given action to the agent and updates its state and reward history.

**Parameters:**

- `state` (numpy array): The current state of the agent.
- `action` (integer): The action the agent should take.
- `reward` (float): The reward for the agent's action.
- `training` (bool): Whether or not the agent is currently training.

### calculateBellmanUpdateValue(self, loc, action)

Calculates the Bellman update for a given state-action pair.

**Parameters:**

- `loc` (integer): The index of the state in the agent's state history.
- `action` (integer): The action the agent took in the state.

**Returns:**

- A list corresponding to the updated Q-values.

### updateWeights(self)

Updates the Q-network weights based on the agent's experiences.

## Example Usage

```python
# Initialize agent
agent = DeepQAgent(input_width=84, input_height=84, action_set_size=4)

# Determine action for current state
state = np.zeros((84, 84, 3))
action = agent.determineAction(state)

# Apply action and update agent state
reward = 1.0
agent.apply(state, action, reward)

# Update agent weights using experience stored in its history
agent.updateWeights()
```