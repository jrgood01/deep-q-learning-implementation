import torch
import DeepQNet
import numpy as np
import random
class Agent():
    def __init__(self, input_width, input_height, action_set_size, model_update_horizon=20, discount_factor=.8, alpha=.8, epsilon_greedy=.1):
        self.model = DeepQNet.Net(input_width, input_height, action_set_size) 
        self.criterion = torch.nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.01)

        self.max_buffer_len = model_update_horizon * 10
        self.model_update_horizon = model_update_horizon
        self.alpha = alpha
        self.discount_factor = discount_factor
        self.epsilon_greedy = epsilon_greedy
        self.action_set_size = action_set_size

        self.state_history = []
        self.action_history = []
        self.reward_history = [0]
        self.inference_history = []


    def determineAction(self, state, epsilon_greedy=True):
        inference = self.model.forward(torch.unsqueeze(state, dim=0))
        self.inference_history.append(inference)
        if epsilon_greedy and random.randint(0, 100) < self.epsilon_greedy * 100:
            return random.randint(0, self.action_set_size - 1)
        return torch.argmax(inference)

    def apply(self, state, action, reward, training=True):
        if len(self.state_history) >= self.max_buffer_len:
            if training:
                self.updateWeights()
            self.state_history = []
            self.action_history = []
            self.reward_history = [0]
            self.inference_history = []
        if training:  
            self.state_history.append(torch.tensor(state.astype(np.float32)))
            self.action_history.append(action)
            self.reward_history.append(reward)
        
    
    def calculateBellmanUpdateValue(self, loc, action):
        #inferenced_q_vals = self.model.forward(torch.tensor(self.state_history[loc].astype(np.float32).T))
        inferenced_q_vals = self.inference_history[loc][0].clone()
        cur_q_val = inferenced_q_vals[action]
        
        next_q_val = max(self.inference_history[loc + 1][0].clone())
        next_reward = self.reward_history[loc + 1]
        bellman_update = (1-self.alpha) * cur_q_val + self.alpha * (next_reward + self.discount_factor * next_q_val)
        ret = inferenced_q_vals
        ret[action] = bellman_update
        return ret

    def updateWeights(self):
        concat_state = []
        for i in range(2, len(self.state_history) - 1):
            concat_state.append(
                torch.stack((
                    self.state_history[i-2], 
                    self.state_history[i-1],
                    self.state_history[i])))

        self.optimizer.zero_grad()
        inputs = torch.stack(concat_state)
        labels = torch.vstack([self.calculateBellmanUpdateValue(v, self.action_history[v]) for v in range(2, len(self.state_history) - 1)])
        outputs = self.model(inputs)
        loss = self.criterion(outputs, labels)
        loss.backward(retain_graph=True)
        self.optimizer.step()
        print("Loss: ",loss)
        print("Avg reward: ", sum(self.reward_history) / len(self.reward_history))