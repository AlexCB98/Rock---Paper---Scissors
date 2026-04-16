import random

print('Use --> 0 for Rock <--, --> 1 for Paper <--, --> 2 for Scissors <--')

user_nr=int(input('Enter your choice: '))
random_nr=random.randint(0,2)

if random_nr==user_nr:
    print("It's a draw! ",'Computer choose: ', random_nr)
elif random_nr==0 and user_nr==1:
    print('You win! ','Computer choose: ', random_nr)
elif random_nr==0 and user_nr==2:
    print('You lose! ','Computer choose: ', random_nr)
elif random_nr==1 and user_nr==0:
    print('You lose! ','Computer choose: ', random_nr)
elif random_nr==1 and user_nr==2:
    print('You win! ','Computer choose: ', random_nr)
elif random_nr==2 and user_nr==0:
    print('You win! ','Computer choose: ', random_nr)
elif random_nr==2 and user_nr==1:
    print('You lose! ','Computer choose: ', random_nr)
else:
    print('You choose an invalid number. You lose! ')
