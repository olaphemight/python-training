"Rock scisscors paper game"
"""Rule of the game
1. Rock win over scisscors
2. paper win over rock
3. scisscors win over paper
"""
import random

scissors = '''     
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'     
'''


paper = """
     /')    ./')             
      /' /.--''./'')           
 :--''  ;    ''./'')          
 :     '     ''./')             
 :           ''./'              
 :--''-..--''''          """

rock = """
                     ''''        ,'        ` .
                               ,'  ,.  ..      `  .
                               `.,'      ..           `
                     __..,.             .  ..     .
                            ` .       .  `.  .` `
                                ,  `.  `.  `._|,..
                                  .  `.  `..'
                                   ` -'`''
"""
game_image = [rock, paper, scissors]
print("Welcome To Rock,Paper, Scissors Game")
"Choose between numbers 0 to 2"

user_choice = int(input("What do you choose?:\n "))
print(f"user Choice:\n {game_image[user_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer Choose: {computer_choice}")

if user_choice >=3 or user_choice < 0:
  print("Ivanlid number, You are to use between 0 to 2 ")
elif user_choice == 0  and computer_choice == 2:
  print(game_image[computer_choice])
  print(f"You win")
elif computer_choice == 0 and user_choice == 2:
  print(game_image[computer_choice])
  print("You loose")
elif computer_choice > user_choice:
  print(game_image[computer_choice])
  print(f"You loose")
elif user_choice > computer_choice :
  print(game_image[computer_choice])
  print(f"You win")
elif user_choice == computer_choice:
  print(game_image[computer_choice])
  print("Draw")
else:
  print("Invalid Number")

