from torch.nn import functional as F
from torch import nn, flatten

class Net(nn.Module):
    def __init__(self, input_width, input_height, action_set_size, bw=True, image_stack_size=3):
        super().__init__()
        input_channels = 3 * image_stack_size if not bw else image_stack_size
        self.conv1 = nn.Conv2d(input_channels, 4, 4)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(4, 8, 2)

        self.fc1 = nn.Linear(30752, 100)
        self.fc2 = nn.Linear(100, 200)
        self.fc3 = nn.Linear(200, action_set_size)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        
        x = flatten(x, 1) 

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x