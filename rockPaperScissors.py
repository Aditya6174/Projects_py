import random
# We input our choice of rock,paper or scissors and the computer chooses one and finally the winner is decided .
def lessPlay():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r' , 'p' , 's'])

    if user == computer :
        return "tie"
    if winner(user,computer) == "true":
        return "you won buddy !"

    return "you lost , computer won"
# r > s s > p p > r

def winner(player,computer) :
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r') :
        return "true"  
 
print(lessPlay())
