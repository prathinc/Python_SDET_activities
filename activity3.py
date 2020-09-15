user1_name = input("Enter 1st player name:")
user2_name = input("Enter 2nd player name:")
user1_input = input(user1_name+"Enter your any one choice out of Rock, Paper and scissors :")
user2_input = input(user2_name+"Enter your any one choice out of Rock, Paper and scissors :")
user1 = user1_input.lower()
user2 = user2_input.lower()

if(user1==user2):
    print("Both players have typed same input")
elif (user1=='rock' and user2 =='paper'):
    print(user2_name+" Wins!!")
elif (user1=='paper' and user2 =='rock'):
    print(user1_name+" Wins!!")
elif (user1=='rock' and user2 =='scissors'):
    print(user1_name+" Wins!!")
elif (user1=='scissors' and user2 =='rock'):
    print(user2_name+" Wins!!")
elif (user1=='paper' and user2 =='scissors'):
    print(user2_name+" Wins!!")
elif (user1=='scissors' and user2 =='paper'):
    print(user1_name+" Wins!!")
else:
    print("You have not entered valid input please try again:")
