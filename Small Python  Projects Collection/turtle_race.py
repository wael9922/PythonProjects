from turtle import Turtle,Screen
import random

screen = Screen()
# setting up th screen size
screen.setup(660,700)
# creating turtles to race them
turtles = [Turtle() for _ in range(6)]
turtle_colors = ["red", "blue", "green", "yellow", "orange", "purple"]

# let the user make a guess
guess = screen.textinput(prompt="Which turtle will win the race?", title="Make your ber:")

for i in range(6):
	turtles[i].shape("turtle")
	turtles[i].color(turtle_colors[i]) # give each turtle a different color
	turtles[i].penup()
	turtles[i].goto(-320, 30*i) # get turtles to the starting positions
	x,y = turtles[i].pos()
	
race_on = True

# start the race
while race_on:
	for t in turtles:
		t.forward(random.randint(1,10))

		if t.xcor()>320:
			race_on = False
			if guess == t.pencolor():
				print(f"{t.pencolor()} turtle wins, You guessed correctly!")
			else:
				print(f"{t.pencolor()} turtle wins, You guessed wrong!")

screen.exitonclick()