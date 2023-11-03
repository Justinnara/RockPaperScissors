import random
import turtle
t=turtle.Turtle()
sOne = turtle.Turtle()
sTwo = turtle.Turtle()
t = turtle.Turtle()
t.speed(0)
p = turtle.Turtle()
rock = turtle.Turtle()

def Drawpaper(x, y):
    p.setheading(0)
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.forward(100)
    p.left(90)
    p.forward(170)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.forward(170)


def Drawrock(x, y):
    rock.penup()
    rock.goto(x, y)
    rock.pendown()
    rock.setheading(0)
    rock.forward(50)
    rock.left(90)
    rock.forward(50)
    rock.left(90)
    rock.forward(50)
    rock.left(90)
    rock.forward(50)
    rock.left(90)


def DrawScissor(x, y):
    sOne.penup()
    sOne.goto(x, y)
    sOne.pendown()
    sOne.setheading(0)
    sTwo.penup()
    sTwo.goto(x,y-80)
    sTwo.pendown()
    sTwo.setheading(0)
    counter = 1
    while counter <= 450:
        sOne.forward(0.5)
        sOne.left(1)
        sTwo.forward(0.5)
        sTwo.left(1)
        counter += 1
    sOne.right(120)
    sOne.forward(170)
    sOne.penup()
    sOne.goto(x, y - 80)
    sOne.pendown()
    sTwo.right(35)
    sTwo.forward(165)


def DrawPC(x, y):
    t.setheading(0)

    t.penup()
    # Original (-340, 200)
    # Start of P
    t.goto(x, y)
    t.pendown()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.right(90)
    t.forward(48)
    # End of P
    t.penup()
    # Original (-250, 200)
    t.goto(x + 45, y)
    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.penup()
    # Original (-250, 200)
    t.goto(x + 45, y)
    t.pendown()
    t.forward(25)


def DrawPlayer(x, y):
    t.setheading(0)

    t.penup()
    # Original (-340, 200)
    t.goto(x, y)
    t.pendown()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)

    t.right(90)

    t.forward(48)

    # End of P
    # Start of L

    t.setheading(270)
    t.penup()
    # Original (-250,200)
    t.goto(x + 50, y)
    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(25)
    # End of L
    # Start of A
    t.penup()
    # Original (-160,200)
    t.goto(x + 90, y)
    t.pendown()
    t.right(100)
    t.forward(60)
    t.penup()
    # Original (-160,200)
    t.goto(x + 90, y)
    t.pendown()
    t.left(110)
    t.right(80)
    t.forward(60)
    t.right(180)
    t.forward(30)
    t.left(70)
    t.forward(20)
    t.penup()
    # End of A
    # Start of Y
    # Original (-70,200)
    t.goto(x + 110, y)
    t.pendown()
    t.penup()
    # Original (-120,200)
    t.goto(x + 110, y)
    t.pendown()
    t.left(120)
    t.forward(30)
    t.right(30)
    t.forward(30)
    t.right(180)
    t.forward(30)
    t.right(30)
    t.forward(30)
    t.penup()
    # End of Y
    # Start of E
    # Orignal (-30,200)
    t.goto(x + 150, y)
    t.pendown()
    t.right(150)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.right(180)
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(180)
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(25)
    # End of E

    # Start of R
    t.penup()
    # Original (60,200)
    t.goto(x + 180, y)
    t.pendown()
    t.right(90)

    t.forward(60)
    t.penup()
    # Orignal (60,200)
    t.goto(x + 180, y)
    t.pendown()
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(130)
    t.forward(45)


def clearDrawings():
    p.clear()
    rock.clear()
    sOne.clear()
    sTwo.clear()

DrawPC(180, 200)
DrawPlayer(-270, 200)


# fourRounds function contains the code for the four rounds game mode.
def fourRounds():
    # Declare variables to keep track of the player, and the computer score
    Playerscore = 0
    Computerscore = 0

    # Loop that will re run main game code, until either the player of the computer reaches a score of 4.
    while Playerscore < 4 and Computerscore < 4:
        Playerpick = input("Enter 1 for Rock, 2 for Paper, 3 for Scissor: ")
        clearDrawings()
        Computerpick = random.randint(1, 3)
        if Computerpick == 1 and Playerpick == "1":
            Drawrock(230, 0)
            Drawrock(-230, 0)
            print("Computer picked Rock")
            print("It's a tie")
        if Computerpick == 1 and Playerpick == "2":
            Drawrock(230, 0)
            Drawpaper(-230, -100)
            print("Computer picked Rock")
            print("Player wins")
            Playerscore += 1
        if Computerpick == 2 and Playerpick == "1":
            Drawpaper(230, -100)
            Drawrock(-230, 0)
            print("Computer picked Paper")
            print("Computer wins")
            Computerscore += 1
        if Computerpick == 1 and Playerpick == "3":
            Drawrock(230, 0)
            DrawScissor(-230, 0)
            print("Computer picked Rock")
            print("Computer wins")
            Computerscore += 1
        if Computerpick == 3 and Playerpick == "1":
            DrawScissor(230, 0)
            Drawrock(-230, 0)
            print("Computer picked Scissor")
            print("Player wins")
            Playerscore += 1
        if Computerpick == 2 and Playerpick == "3":
            Drawpaper(230, -100)
            DrawScissor(-230, 0)
            print("Computer picked Paper")
            print("Player wins")
            Playerscore += 1
        if Computerpick == 3 and Playerpick == "3":
            DrawScissor(230, 0)
            DrawScissor(-230, 0)
            print("Computer picked Scissor ")
            print("It's a tie")
        if Computerpick == 3 and Playerpick == "2":
            DrawScissor(200, 0)
            Drawpaper(-230, -100)
            print("Computer picked Scissor")
            print("Computer Wins")
            Computerscore += 1
        if Computerpick == 2 and Playerpick == "2":
            Drawpaper(230, -100)
            Drawpaper(-230, -100)
            print("Computer picked Paper")
            print("It's a tie")
        print("The player score is: ", Playerscore)
        print("The computer score is: ", Computerscore)
    print("GAME OVER ")


def UnlimitedRounds():
    Computerscore = 0
    Playerscore = 0
    print("unlimited rounds")
    while True:
        Playerpick = input("Enter 1 for Rock, 2 for Paper, 3 for Scissor: ")
        clearDrawings()
        Computerpick = random.randint(1, 3)
        if Computerpick == 1 and Playerpick == "1":
            print("Computer picked Rock")
            print("It's a tie")
            Drawrock(230, 0)
            Drawrock(-230, 0)
        if Computerpick == 1 and Playerpick == "2":
            print("Computer picked Rock")
            print("Player wins")
            Drawrock(230, 0)
            Drawpaper(-230, -100)
            Playerscore += 1
        if Computerpick == 2 and Playerpick == "1":
            print("Computer picked Paper")
            print("Computer wins")
            Drawpaper(230, -100)
            Drawrock(-230, 0)
            Computerscore += 1
        if Computerpick == 1 and Playerpick == "3":
            print("Computer picked Rock")
            print("Computer wins")
            Drawrock(230, 0)
            DrawScissor(-230, 0)
            Computerscore += 1
        if Computerpick == 3 and Playerpick == "1":
            print("Computer picked Scissor")
            print("Player wins")
            DrawScissor(230, 0)
            Drawrock(-230, 0)
            Playerscore += 1
        if Computerpick == 2 and Playerpick == "3":
            print("Computer picked Paper")
            print("Player wins")
            Drawpaper(230, -100)
            DrawScissor(-230, 0)
            Playerscore += 1
        if Computerpick == 3 and Playerpick == "3":
            print("Computer picked Scissor ")
            print("It's a tie")
            DrawScissor(230, 0)
            DrawScissor(-230, 0)
        if Computerpick == 3 and Playerpick == "2":
            print("Computer picked Scissor")
            print("Computer Wins")
            DrawScissor(230, 0)
            Drawpaper(-230, -100)
            Computerscore += 1
        if Computerpick == 2 and Playerpick == "2":
            print("Computer picked Paper")
            print("It's a tie")
            Drawpaper(230, -100)
            Drawpaper(-230, -100)
        print("The player score is: ", Playerscore)
        print("The computer score is: ", Computerscore)


# Start of the main program
Menu = input("Enter 1 for first to reach 4, Enter 2 for unlimited rounds: ")
if Menu == "1":
    fourRounds()
elif Menu == "2":
    UnlimitedRounds()