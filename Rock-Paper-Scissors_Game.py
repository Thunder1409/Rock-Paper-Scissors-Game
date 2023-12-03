import random

points = int(input("Enter the max points -: "))

com_points, user_points = 0, 0

while(com_points <= points and user_points <= points):

    print("1. Rock \n2. Paper \n3. Scissor")
    user = int(input("Enter your option -: "))

    comuter = random.randrange(1, 3)

    if (comuter == 1):
        com = "Rock"

    elif (comuter == 2):
        com = "Paper"

    else:
        com = "Scissor"

    print("\nComputer choose -: ", com, "\n")

    if(user == 1 and comuter == 3 or user == 2 and comuter == 1 or user == 3 and comuter == 2):
        print("You won")
        user_points = user_points + 1

    elif(comuter == 1 and user == 3 or comuter == 2 and user == 1 or comuter == 3 and user == 2):
        print("Computer won")
        com_points = com_points + 1

    else:
        print("Draw")

    print("Points -: ", com_points, " - ", user_points)
    print("-------------------------------------------------------------------------------------------------------------")