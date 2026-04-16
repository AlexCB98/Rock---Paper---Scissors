import random

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

print('Use --> 0 for Rock <--, --> 1 for Paper <--, --> 2 for Scissors <--\n')
user_nr=int(input('Enter your choice: '))
random_nr=random.randint(0,2)
joc=[rock, paper, scissors]

if random_nr==user_nr:
    print("It's a draw! ",joc[user_nr],'Computer: ',joc[random_nr])
elif random_nr==0 and user_nr==1:
    print('You win! ',joc[user_nr],'Computer: ',joc[random_nr])
elif random_nr==0 and user_nr==2:
    print('You lose! ',joc[user_nr],'Computer: ',joc[random_nr])
elif random_nr==1 and user_nr==0:
    print('You lose! ',joc[user_nr],'Computer: ',joc[random_nr])
elif random_nr==1 and user_nr==2:
    print('You win! ',joc[user_nr],'Computer: ',joc[random_nr])
elif random_nr==2 and user_nr==0:
    print('You win! ',joc[user_nr],'Computer: ',joc[random_nr])
elif random_nr==2 and user_nr==1:
    print('You lose! ',joc[user_nr],'Computer: ',joc[random_nr])
else:
    print('You choose an invalid number. You lose! ')
