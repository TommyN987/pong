import turtle

window = turtle.Screen()
window.title("PyPong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

class Player:
	def __init__(self, name, color, side):
		self.name = name
		self.score = 0
		self.color = color
		self.paddle = turtle.Turtle()
		self.paddle.speed(0)
		self.paddle.shape("square")
		self.paddle.color(color)
		self.paddle.shapesize(stretch_wid=5, stretch_len=1)
		self.paddle.penup()
        
		if side == "left":
			self.paddle.goto(-350, 0)
		elif side == "right":
			self.paddle.goto(350, 0)

	def increment_score(self):
		self.score += 1
	
	def move_up(self):
		y = self.paddle.ycor()
		y += 20
		if y <= 240:
			self.paddle.sety(y)
	
	def move_down(self):
		y = self.paddle.ycor()
		y -= 20
		if y >= -240:
			self.paddle.sety(y)

player_1 = Player("Player 1", "purple", "left")
player_2 = Player("Player 2", "red", "right")

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -.04
ball.dy = -.04

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

def game_over():
	winner = ""
	color = ""

	if (player_1.score > player_2.score):
		winner = player_1.name
		color = player_1.color
	else:
		winner = player_1.name
		color = player_1.color

	gameover_pen = turtle.Turtle()
	gameover_pen.speed(0)
	pen.color(color)
	pen.penup()
	pen.hideturtle()
	pen.goto(0, 160)
	pen.write("{} wins!".format(winner), align="center", font=("Courier", 24, "normal"))

# Keyboard binding
window.listen()
window.onkeypress(player_1.move_up, "w")
window.onkeypress(player_1.move_down, "s")
window.onkeypress(player_2.move_up, "Up")
window.onkeypress(player_2.move_down, "Down")

# main loop
while True:
	window.update()

	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1	
	
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
	
	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		player_1.increment_score()
		pen.clear()
		pen.write("Player 1: {}  Player 2: {}".format(player_1.score, player_2.score), align="center", font=("Courier", 24, "normal"))
	
	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		player_2.increment_score()
		pen.clear()
		pen.write("Player 1: {}  Player 2: {}".format(player_1.score, player_2.score), align="center", font=("Courier", 24, "normal"))

	# Collisions
	if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < player_2.paddle.ycor() + 50 and ball.ycor() > player_2.paddle.ycor() - 50):
		ball.setx(330)
		ball.dx *= -1

	if (ball.xcor() > -340 and ball.xcor() < -330) and (ball.ycor() < player_1.paddle.ycor() + 50 and ball.ycor() > player_1.paddle.ycor() - 50):
		ball.setx(-330)
		ball.dx *= -1
	
	if player_1.score == 10 or player_2.score == 10:
		ball.goto(0, 0)
		ball.dx = 0
		ball.dy = 0
		game_over()