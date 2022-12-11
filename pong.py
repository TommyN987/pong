import turtle

window = turtle.Screen()
window.title("PyPong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

class Game:
	def __init__(self):
		self.is_over = False
		self.scores = {"Player_1" : 0, "Player_2": 0}
		self.scoreboard = turtle.Turtle()
		self.scoreboard.speed(0)
		self.scoreboard.color("white")
		self.scoreboard.penup()
		self.scoreboard.hideturtle()
		self.scoreboard.goto(0, 260)
		self.scoreboard.write("Player 1: {}  Player 2: {}".format(self.scores["Player_1"], self.scores["Player_2"]), align="center", font=("Courier", 24, "normal"))
	
	def increment(self, player):
		if player == 1:
			self.scores["Player_1"] += 1
			self.update_scoreboard()
			if self.scores["Player_1"] == 10:
				self.is_over = True
			
		elif player == 2:
			self.scores["Player_2"] += 1
			self.update_scoreboard()
			if self.scores["Player_2"] == 10:
				self.is_over = True
	
	def update_scoreboard(self):
		self.scoreboard.clear()
		self.scoreboard.write("Player 1: {}  Player 2: {}".format(self.scores["Player_1"], self.scores["Player_2"]), align="center", font=("Courier", 24, "normal"))
	
	def game_over(self, player_1, player_2):
		winner = ""
		color = ""

		if self.scores["Player_1"] > self.scores["Player_2"]:
			winner = player_1.name
			color = player_1.color
		else:
			winner = player_2.name
			color = player_2.color

		gameover_pen = turtle.Turtle()
		gameover_pen.speed(0)
		gameover_pen.color(color)
		gameover_pen.penup()
		gameover_pen.hideturtle()
		gameover_pen.goto(0, 160)
		gameover_pen.write("{} wins!".format(winner), align="center", font=("Courier", 24, "normal"))

class Player:
	def __init__(self, name, color, side):
		self.name = name
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

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -.05
ball.dy = -.05

player_1 = Player("Player 1", "purple", "left")
player_2 = Player("Player 2", "red", "right")
game = Game()

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
		game.increment(1)
	
	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		game.increment(2)

	# Collisions
	if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < player_2.paddle.ycor() + 50 and ball.ycor() > player_2.paddle.ycor() - 50):
		ball.setx(330)
		ball.dx *= -1

	if (ball.xcor() > -340 and ball.xcor() < -330) and (ball.ycor() < player_1.paddle.ycor() + 50 and ball.ycor() > player_1.paddle.ycor() - 50):
		ball.setx(-330)
		ball.dx *= -1
	
	if game.is_over:
		ball.goto(0, 0)
		ball.dx = 0
		ball.dy = 0
		game.game_over(player_1, player_2)