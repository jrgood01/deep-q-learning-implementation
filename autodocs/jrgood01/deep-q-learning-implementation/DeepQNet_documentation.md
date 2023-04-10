# DeepQNet.py Documentation

## Code Summary

The `DeepQNet.py` file contains the code for the `Net` class, which defines a neural network model used in the Deep Q-learning algorithm.

The `Net` class extends the `nn.Module` class from the torch library, and defines the neural network layers present in the model using the `__init__` method. This includes convolutional layers, max pooling layers, and fully connected layers.

The `forward` method of the `Net` class is used to define the forward pass of the neural network, taking in an input data tensor and returning the output logits tensor.

## Class Summaries

### Net

Class that defines a neural network model used in the Deep Q-learning algorithm.

#### Methods

| Method | Description |
| --- | --- |
| `__init__(self, input_width, input_height, action_set_size, bw=True, image_stack_size=3)` | Initializes the neural network model with `input_width`, `input_height`, and `action_set_size`. Defines the neural network layers present in the model, including convolutional layers, max pooling layers, and fully connected layers. |
| `forward(self, x)` | Defines the forward pass of the neural network, taking in an input data tensor and returning the output logits tensor. |

## Method Summaries

### Net.__init__(self, input_width, input_height, action_set_size, bw=True, image_stack_size=3)

Initializes the neural network model with `input_width`, `input_height`, and `action_set_size`. Defines the neural network layers present in the model, including convolutional layers, max pooling layers, and fully connected layers.

Parameters:
- `input_width`: The width of the input data.
- `input_height`: The height of the input data.
- `action_set_size`: The number of possible actions in the environment.
- `bw`: A boolean indicating whether to use grayscale or color images. Default is `True` for grayscale.
- `image_stack_size`: The number of frames to stack together as input. Default is `3`.

Example usage:
```python
net = Net(input_width=84, input_height=84, action_set_size=4)
```

### Net.forward(self, x)

Defines the forward pass of the neural network, taking in an input data tensor and returning the output logits tensor.

Parameters:
- `x`: The input data tensor.

Returns:
- The output logits tensor.

Example usage:
```python
output_logits = net.forward(input_data)
```

## Example Usage

```python
from DeepQNet import Net

# Create a neural network model
net = Net(input_width=84, input_height=84, action_set_size=4)

# Pass input data through the model
input_data = torch.randn(1, 3, 84, 84)
output_logits = net.forward(input_data)
```