# DeepQNet.py

## Code Summary

This file defines the neural network architecture for the Deep Q-Network class. The class 'Net' inherits from the torch.nn.Module class and includes the following layers:
- 2 convolutional layers with ReLU activation functions
- 3 fully connected layers with ReLU activation functions, including the output layer

The 'Net' class has a forward method which overrides the forward method of the parent class. The forward method defines the flow of the input tensor through the layers of the network.

## Class Summaries

### Net
The `Net` class defines the neural network architecture for the Deep Q-Network. The class inherits from the `torch.nn.Module` class and contains the following layers:
    
- Two 2D convolutional layers with ReLU activation function
- A max pooling layer to downsample the input for the convolutional layers
- Three fully connected (linear) layers with ReLU activation function
- An output layer

The `forward` method of the `Net` class propagates the input tensor through these layers to produce the output.

### Parameters:
- `input_width` : Width of input images (int)
- `input_height` : Height of input images (int)
- `action_set_size` : Possible number of actions (int)
- `bw` : Boolean indicating whether input images are black and white (default: True)
- `image_stack_size` : Number of images the network will see in a sequence (default: 3)

### Output:
- An initialized object of the `Net` class.

## Method Summaries

### Net.forward(self, x)
Propagates the input tensor through the network layers to produce the action values.

### Parameters:
- `x` : Input tensor to the network.

### Output:
- A tensor of action values for each possible action.

## Example Usage
```python
import torch
from DeepQNet import Net

input_width = 84
input_height = 84
action_set_size = 4

net = Net(input_width, input_height, action_set_size)
```
Here, we initialize an object 'net' for the DeepQNet class with input_width=84, input_height=84, and action_set_size=4. 

```python
output = net.forward(torch.Tensor(3, 3, 84, 84))
```
This generates the output tensor by propagating the tensor with a size of 3 x 3 x 84 x 84 through the 'net' object using the forward method.