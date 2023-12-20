from turtle import Screen,Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake():
    
    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]


    def create_snake(self):

        # Create a snake body
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        # 3 Turtle object segments for snake body
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.up()
        # position the 3 parts at 0,-20,-40
        snake_segment.goto(position)

        # Attach the 3 parts to the snake body
        self.snake_body.append(snake_segment)


    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        # Snake movement
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


