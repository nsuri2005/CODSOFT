import random
def game(user_choice,computer_choice):
    if(user_choice=="rock" and computer_choice=="scissor")or(user_choice=="scissor" and computer_choice=="paper")or(user_choice=="paper" and computer_choice=="rock"):
        print("wins")
    elif(user_choice==computer_choice):
        print("tie")
    else:
        print("loss")
list=["rock","paper","scissor"]
loop=2
while(loop!=0):
    computer_choice=random.choice(list)
    user_choice=input("enter your choice (eg:rock paper,scissor):")
    print("your choice:",user_choice)
    print("computer_choice:",computer_choice)  
    game(user_choice,computer_choice)
    loop=int(input("do you want to continue 2.yes 0.no:"))
