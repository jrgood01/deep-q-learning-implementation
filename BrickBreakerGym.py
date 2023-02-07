from ipycanvas import Canvas, hold_canvas
from ipywidgets import Output
import random

out = Output()

class Brick():
    def __init__(self, x, y, width, height, lives=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lives = lives

    def isOverlapping(self, x, y, width, height):
        return x >= self.x and y >= self.y and x + width <= self.x + self.width and y + height <= self.y + self.height
    
    def getColor(self):
        return [0, 0, 0]

class BrickBreakerGym():
    def __init__(self, res_x, res_y, y_fill_proportion=.5, brick_inlay_proportion=.3, brick_width=100, brick_height=20):
        self.res_x = res_x
        self.res_y = res_y
        self.canvas = Canvas(width=res_x, height=res_y, sync_image_data=True)
        self.canvas.layout.width = str(res_x)+'px'
        self.canvas.layout.height = str(res_y)+'px'
        self.canvas.alpha = 0
        self.bricks = []

        self.paddle_width = 150
        self.paddle_height = 20

        self.paddle_x = 30
        self.paddle_y = self.res_y - self.paddle_height

        self.ball_x = 50
        self.ball_y = self.paddle_y - 20
        self.ball_dx = 1
        self.ball_dy = -.5

        self.reward = 0


        self.canvas.on_key_down(self.on_keyboard_event)

        x_step = brick_width + 2
        y_step = (brick_height + 2)
        for x in range(0, int(res_x / x_step)):
            start_x = x * x_step
    
            for y in range(0, int(brick_inlay_proportion * res_y / y_step)):
                start_y = y * y_step
                if random.randint(0, 100) < brick_inlay_proportion * 100:
                    self.bricks.append(Brick(start_x, start_y, brick_width, brick_height))

    def startRender(self):
        display(self.canvas)
    
    def detectBrickHit(self):
        for brick in self.bricks:
            if brick.isOverlapping(self.ball_x, self.ball_y, 10, 10):
                brick.lives -= 1
                self.reward += 1
                self.ball_dy = -self.ball_dy
                return True
            return False

    def flip(self):
        with hold_canvas():
            self.canvas.clear()

            brick_x = [brick.x for brick in self.bricks]
            brick_y = [brick.y for brick in self.bricks]

            brick_width = [brick.width for brick in self.bricks]
            brick_height = [brick.height for brick in self.bricks]

            brick_color = [brick.getColor() for brick in self.bricks]

            self.canvas.fill_styled_rects(brick_x, brick_y, brick_width, brick_height, brick_color)
            self.canvas.fill_styled_rects([self.paddle_x], [self.paddle_y], [self.paddle_width], [self.paddle_height], [[50, 50, 50]])

            self.canvas.fill_styled_circles([self.ball_x], [self.ball_y], [10], [0, 0, 0])

            if self.ball_x > self.res_x - 10:
                self.ball_dx = -self.ball_dx + (random.randint(0, 10) - 5) / 10
            
            if self.ball_x <= 0:
                self.ball_dx = -self.ball_dx + (random.randint(0, 10) - 5) / 10
            
            if self.ball_y <= 0:
                self.ball_dy = -self.ball_dy

            self.ball_x += self.ball_dx
            self.ball_y += self.ball_dy

            self.detectBrickHit()


    def paddle_right(self):
        self.paddle_x += 2
    
    def paddle_left(self):
        self.paddle_y -= 2

    @out.capture()
    def on_keyboard_event(self, key, shift_key, ctrl_key, meta_key):
        print("down")
        self.paddle_x -= 5
