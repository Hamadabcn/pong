import turtle
import winsound
import pygame

# Initialize the mixer for sound effects
pygame.mixer.init()
pygame.mixer.Sound("bounce.wav").play()

# Set up the game window
wn = turtle.Screen()
wn.title("Pong by Hamadabcn")  # Title of the game window
wn.bgcolor("black")  # Background color of the window
wn.setup(width=800, height=600)  # Set the dimensions of the window
wn.tracer(0)  # Turn off-screen updates for better performance

# Initialize scores
score_a = 0
score_b = 0

# Set up paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Set the speed of the paddle to the maximum
paddle_a.shape("square")  # Shape of the paddle
paddle_a.color("white")  # Color of the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Size of the paddle
paddle_a.penup()  # Prevent drawing lines when the paddle moves
paddle_a.goto(-370, 0)  # Position the paddle A on the left side

# Set up paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Set the speed of the paddle to the maximum
paddle_b.shape("square")  # Shape of the paddle
paddle_b.color("white")  # Color of the paddle
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # Size of the paddle
paddle_b.penup()  # Prevent drawing lines when the paddle moves
paddle_b.goto(370, 0)  # Position the paddle B on the right side

# Set up the ball
ball = turtle.Turtle()
ball.speed(0)  # Set the speed of the ball to the maximum
ball.shape("square")  # Shape of the ball
ball.color("white")  # Color of the ball
ball.penup()  # Prevent drawing lines when the ball moves
ball.goto(0, 0)  # Start the ball at the center of the screen
ball.dx = 0.15  # Ball's speed in the x direction
ball.dy = 0.15  # Ball's speed in the y direction

# Set up the score display
pen = turtle.Turtle()
pen.speed(0)  # Set the speed of the pen to the maximum
pen.color("white")  # Color of the score text
pen.penup()  # Prevent drawing lines when moving the pen
pen.hideturtle()  # Hide the pen turtle
pen.goto(0, 260)  # Position the score display at the top of the screen
pen.write("Player X: 0  Player Y: 0", align="center", font=("Courier", 24, "normal"))


# Functions to move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20  # Move paddle A up by 20 units
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20  # Move paddle A down by 20 units
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20  # Move paddle B up by 20 units
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20  # Move paddle B down by 20 units
    paddle_b.sety(y)


# Keyboard bindings to control paddles
wn.listen()  # Listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")  # Bind 'w' key to move paddle A up
wn.onkeypress(paddle_a_down, "s")  # Bind 's' key to move paddle A down
wn.onkeypress(paddle_b_up, "Up")  # Bind 'Up' arrow key to move paddle B up
wn.onkeypress(paddle_b_down, "Down")  # Bind 'Down' arrow key to move paddle B down

# Game over condition
max_score = 10  # Score required to win the game

# Main game loop
while True:
    wn.update()  # Update the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Check collision with top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse the ball's direction
        winsound.PlaySound("./bounce.wav", winsound.SND_ASYNC)  # Play bounce sound

    # Check collision with bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Reverse the ball's direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound

    # Check if ball goes off the left side
    if ball.xcor() > 350:
        ball.goto(0, 0)  # Reset ball to center
        ball.dx *= -1  # Reverse the ball's direction
        score_a += 1  # Increase score for player X
        pen.clear()  # Clear previous score display
        pen.write("Player X: {}  Player Y: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Check if ball goes off the right side
    if ball.xcor() < -350:
        ball.goto(0, 0)  # Reset ball to center
        ball.dx *= -1  # Reverse the ball's direction
        score_b += 1  # Increase score for player Y
        pen.clear()  # Clear previous score display
        pen.write("Player X: {}  Player Y: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    # Check collision with paddle B
    if (340 < ball.xcor() < 350) and (
            paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1  # Reverse the ball's direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound

    # Check collision with paddle A
    if (-340 > ball.xcor() > -350) and (
            paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1  # Reverse the ball's direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound

    # Check for game over
    if score_a == max_score or score_b == max_score:
        winner = "Player X" if score_a == max_score else "Player Y"  # Determine the winner
        pen.clear()  # Clear the score display
        pygame.mixer.Sound("game_over.wav").play()  # Play game over sound
        pen.write("{} wins! Game Over".format(winner), align="center", font=("Courier", 24, "normal"))  # Display the winner
        wn.mainloop()  # This allows the window to close
        break
