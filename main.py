import random
print("What do you choice ? type 0 for Rock, 1 for paper, 2 for scissors")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
join=[rock,paper,scissors]
computer_choice = random.randint(0,2)
player_choice = int(input("Enter your choice : "))

print("Your choice is :")
print(join[player_choice])

print("Computer choice is :"+join[computer_choice])

if(player_choice>2 or player_choice<0):
  print("wrong input........YOU LOSS!!")
elif(computer_choice ==player_choice):
  print("Draw")
elif(player_choice==0 and computer_choice ==2):
  print("You Win!!!")
  
elif(player_choice==1 and computer_choice ==0):
    print("You Win!!!")
  
elif(player_choice==2 and computer_choice ==1):
    print("You Win!!!")
else:
  print("YOU LOSS!!!")  
    
