import turtle

wn = turtle.Screen()
wn.setup(width=700,height=400)
wn.title("Python Turtle Movement")

def playerUp():
  player.sety(player.ycor()+10)
def playerDown():
  player.sety(player.ycor()-10)
def playerRight():
  player.setx(player.xcor()+10)
def playerLeft():
  player.setx(player.xcor()-10)

player = turtle.Turtle()
player.speed(0) #this will make your player created instantly
player.shape("square") #set player shape
player.color("red") #set player color
player.penup() #prevent drawing lines
player.goto(0,0) #set player location

wn.onkeypress(playerUp, "w") #function, key
wn.onkeypress(playerDown, "s")
wn.onkeypress(playerRight, "d")
wn.onkeypress(playerLeft, "a")

#update the window
while True:
  wn.update()