#setting up the game
help=open('help.txt','r')
     
import sys
print(format('Welcome to the Soldier of Fortune','^20'))

#getting users choice

Choice = input('\nDo you want to play the game \nY/N : ')
Choice.lower()
if 'y' in Choice:
    print('\nOk Then lets begin!!\n')
else:
    print('\nSee you next time\n')
    exit
    
#beginning the game
#setting up variable
    
end=0
easter1=0
easter2=0

#commencing the game
print('\nType help if you have any doubts')
print('\nType your commands the game will execute them\n')
print(format('Preface','^20'))
print('\nMax is a soldier for the allied forces, At the war in the battlefield of Berlin,\
He was mortally wounded in the battlefield and lost his consciousness. The allied army retreats. \
He is presumed dead by his team and is left to dead on the battlefield. \
When he regains consciousness ,He is finds himself on the hospital bed. \
But to his dismay it was the enemy basecamp, the head of the nazi bootcamp saved him thinking he was some \
commanding officer of the allied forces and thought of extracting intel from him once max regained his \
conscious.')

while end==0:
    move=input('\nEnter your move: ')
    move=move.lower()
    if 'help' in move:
        print()
        print(help.read())
        help.seek(0)
        continue
    if move == 'exit' :
        print('Thanks for playing')
        sys.exit()
    else:
        print('Not a valid command')
        