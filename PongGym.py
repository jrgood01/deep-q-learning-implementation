from RLGym import Gym
import random

class Paddle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        
    def drawPaddle(self, curState):
        curState[self.y:(self.y+self.h), self.x:(self.x + self.w)] = 255

    def detectHit(self, x, y, w, h):
        '''     rect1.x < self.x + self.w and \
                rect1.x + rect1.w > self.x and \
                rect1.y < self.y + self.h and \
                rect1.h + rect1.y > self.y
        '''
        return x < self.x + self.w and \
               x + w > self.x and \
               y < self.y + self.h and \
               h + y > self.y

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.dx = 7
        self.dy = 7

    def drawBall(self, curState):
        curState[self.y:(self.y+5), self.x:(self.x + 5)] = 255

class PongGym(Gym):
    def __init__(self, width, height):
        super().__init__(width, height, 9)
        self.paddleL = Paddle(0, 30, 10, 20)
        self.paddleR = Paddle(self.width - 10, 30, 10, 20)
        self.ball = Ball(100, 100)

    def paddleRUp(self):
        if self.paddleR.y + 3 + self.paddleR.h <= self.height:
            self.paddleR.y += 3
    def paddleRDown(self):
        if self.paddleR.y - 3 >= 0:
            self.paddleR.y -= 3
    def paddleLUp(self):
        if self.paddleL.y + 3 + self.paddleR.h <= self.height:
            self.paddleL.y += 3        
    def paddleLDown(self):
        if self.paddleL.y - 3 >= 0:
            self.paddleL.y -= 3

    def applyAction(self, action):
        if action == 0:
            if self.paddleL.y - 3 >= 0:
                self.paddleL.y -= 3
        if action == 1:
            if self.paddleL.y + 3 + self.paddleR.h <= self.height:
                self.paddleL.y += 3
        if action == 2:
            if self.paddleR.y - 3 >= 0:
                self.paddleR.y -= 3
        if action == 3:
            if self.paddleR.y + 3 + self.paddleR.h <= self.height:
                self.paddleR.y += 3
        if action == 4:
            self.paddleLDown()
            self.paddleRDown()
        if action == 5:
            self.paddleLUp()
            self.paddleRUp()
        if action == 6:
            self.paddleLUp()
            self.paddleRDown()
        if action == 7:
            self.paddleLDown()
            self.paddleRUp()
            
        return self.update()


    def update(self):
        self.ball.x += self.ball.dx
        self.ball.y += self.ball.dy

        if self.paddleL.detectHit(self.ball.x, self.ball.y, 5, 5) or self.paddleR.detectHit(self.ball.x, self.ball.y, 10, 10):
            dx_r = random.randint(-3, 3)
            dy_r = random.randint(-3, 3)

            self.ball.dx = -self.ball.dx + (dx_r if dx_r != -self.ball.dx else 0)
            self.ball.dy = -self.ball.dy + (dy_r if dy_r != -self.ball.dy else 0)

            return 100
        
        if self.ball.x < 0 or self.ball.x + 5 > self.width:
            self.ball.x = random.randint(30, 200)
            self.ball.y = random.randint(30, 200)
            return -100

        if self.ball.y < 0 or self.ball.y + 5 > self.height:
            self.ball.dy = -self.ball.dy

        self.clear_state()

        self.paddleL.drawPaddle(self.state)
        self.paddleR.drawPaddle(self.state)
        self.ball.drawBall(self.state)

        return 0

    def reset(self):
        self.paddleL.y = random.randint(0, 200)
        self.paddleR.y = random.randint(0, 200)

        self.ball.x = random.randint(50, 200)
        self.ball.y = random.randint(0, 200)
        
        self.ball.dx = random.randint(-3, 3)
        self.ball.dy = random.randint(-3, 3)

        if self.ball.dx == 0:
            self.ball.dx = -1
        if self.ball.dy == 0:
            self.ball.dy = -1



        