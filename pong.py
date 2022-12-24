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

		self.top_border = turtle.Turtle()
		self.top_border.speed(0)
		self.top_border.shape("square")
		self.top_border.shapesize(stretch_wid=1, stretch_len=40)
		self.top_border.goto(0,310)
		self.top_border.color("white")
		self.top_border.penup()

		self.bottom_border = turtle.Turtle()
		self.bottom_border.speed(0)
		self.bottom_border.shape("square")
		self.bottom_border.shapesize(stretch_wid=1, stretch_len=40)
		self.bottom_border.goto(0,-310)
		self.bottom_border.color("white")
		self.bottom_border.penup()

		self.right_border = turtle.Turtle()
		self.right_border.speed(0)
		self.right_border.shape("square")
		self.right_border.shapesize(stretch_wid=32, stretch_len=1)
		self.right_border.goto(410,0)
		self.right_border.color("white")
		self.right_border.penup()

		self.left_border = turtle.Turtle()
		self.left_border.speed(0)
		self.left_border.shape("square")
		self.left_border.shapesize(stretch_wid=32, stretch_len=1)
		self.left_border.goto(-410,0)
		self.left_border.color("white")
		self.left_border.penup()

		self.scoreboard = turtle.Turtle()
		self.scoreboard.speed(0)
		self.scoreboard.color("white")
		self.scoreboard.penup()
		self.scoreboard.hideturtle()
		self.scoreboard.goto(0, 240)
		self.scoreboard.write("Player 1: {}  Player 2: {}".format(self.scores["Player_1"], self.scores["Player_2"]), align="center", font=("Courier", 24, "normal"))

		self.ball = turtle.Turtle()
		self.ball.speed(0)
		self.ball.shape("circle")
		self.ball.color("white")
		self.ball.penup()
		self.ball.goto(0, 0)
		self.ball.dx = -.05
		self.ball.dy = -.05

		self.gameover_pen = turtle.Turtle()
	
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

		self.gameover_pen.speed(0)
		self.gameover_pen.color(color)
		self.gameover_pen.penup()
		self.gameover_pen.hideturtle()
		self.gameover_pen.goto(0, 160)
		self.gameover_pen.write("{} wins!".format(winner), align="center", font=("Courier", 24, "normal"))
	
	def new_game(self):
		if (self.is_over == True):
			self.scores["Player_1"] = 0
			self.scores["Player_2"] = 0
			self.update_scoreboard()
			self.gameover_pen.clear()
			self.is_over = False
			self.ball.dx = -.05
			self.ball.dy = -.05

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

player_1 = Player("Player 1", "yellow", "left")
player_2 = Player("Player 2", "green", "right")
game = Game()

window.listen()
	# Keyboard binding
window.onkeypress(player_1.move_up, "w")
window.onkeypress(player_1.move_down, "s")
window.onkeypress(player_2.move_up, "Up")
window.onkeypress(player_2.move_down, "Down")
window.onkeypress(game.new_game, "n")

# main loop
while True:
	window.update()

	# Move the ball
	game.ball.setx(game.ball.xcor() + game.ball.dx)
	game.ball.sety(game.ball.ycor() + game.ball.dy)

	# Border checking
	if game.ball.ycor() > 290:
		game.ball.sety(290)
		game.ball.dy *= -1	
	
	if game.ball.ycor() < -290:
		game.ball.sety(-290)
		game.ball.dy *= -1
	
	if game.ball.xcor() > 390:
		game.ball.goto(0, 0)
		game.ball.dx *= -1
		game.increment(1)
	
	if game.ball.xcor() < -390:
		game.ball.goto(0, 0)
		game.ball.dx *= -1
		game.increment(2)

	# Collisions
	if (game.ball.xcor() > 330 and game.ball.xcor() < 340) and (game.ball.ycor() < player_2.paddle.ycor() + 50 and game.ball.ycor() > player_2.paddle.ycor() - 50):
		game.ball.setx(330)
		game.ball.dx *= -1

	if (game.ball.xcor() > -340 and game.ball.xcor() < -330) and (game.ball.ycor() < player_1.paddle.ycor() + 50 and game.ball.ycor() > player_1.paddle.ycor() - 50):
		game.ball.setx(-330)
		game.ball.dx *= -1
	
	if game.is_over:
		game.ball.goto(0, 0)
		game.ball.dx = 0
		game.ball.dy = 0
		game.game_over(player_1, player_2)