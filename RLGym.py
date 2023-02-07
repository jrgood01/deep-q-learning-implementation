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

class Gym():
    def __init__(self, width, height, action_set_size, render=True):
        self.width = width
        self.height = height
        self.action_set_size = action_set_size
        self.state = np.zeros((width, height), np.uint8) * 128
        self.agent = DeepQAgent.Agent(width, height, action_set_size)

        IPython.display.display(PIL.Image.fromarray(self.state, mode='L'), display_id='0')

    def clear_state(self):
        self.state = np.zeros((self.width, self.height), np.uint8) * 128

    @abstractmethod
    def applyAction(self, action):
        pass

    def updateState(self, training=True):
        log_state = self.state

        if len(self.agent.state_history) > 1:
            state = torch.stack((
                torch.tensor(self.agent.state_history[-2]),
                torch.tensor(self.agent.state_history[-1]),
                torch.tensor(self.state)
            ))
            best_action = self.agent.determineAction(state, epsilon_greedy=training)
        else:
            best_action = random.randint(0, self.action_set_size)
            if training:
                self.agent.inference_history.append(None)
        reward = self.applyAction(best_action)
        
        self.agent.apply(log_state, best_action, reward, training=training)



    def render(self):
        IPython.display.update_display(PIL.Image.fromarray(self.state, mode="L"), display_id='0')