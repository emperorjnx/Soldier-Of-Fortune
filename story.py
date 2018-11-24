import functions as f
import time
import sys
records = open('records.txt','w+')

with open('Scenario.txt','r') as scene:
    story = scene.readlines()

story1 = story[16:36]

def s1():
    f.audioplayer('scene-1')
    global story1
    global records
    move=input('Do you want to enter the battle field?\n')
    if 'y' in move:
        print()
        f.slow_type('Playing a clip')
        f.play('droping in the field')
        f.audioplayer('scene-1')
        for i in range(0,4):
            f.slow_type(story1[i])
        print()
        time.sleep(2)
        move = input('Do you want to make your way to your battalion?\n')
        if 'y' in move:
            print()
            for i in range(4,14):
                f.slow_type(story1[i])
            print()
            f.slow_type('Playing a clip')
            f.play('intro')
            f.slow_type('You somehow survive')
            time.sleep(2)
            f.play('intro 2')
            f.audioplayer('scene-1')
            for i in range(14,20):
                f.slow_type(story1[i])
            print()
        else:
            f.slow_type('\nYou feel that going to your battalion is not safe and you venture alone')
            f.slow_type('\nBy mistake you step on a mine')
            f.slow_type('\nYOU DIE!!',0.25)
            f.slow_type('\nTHE END',0.25)
            sys.exit()
    else:
        move = input('Do you want to make your way to your battalion?\n')
        if 'y' in move or 'ok' in move:
            print()
            for i in range(4,14):
                f.slow_type(story1[i])
            print()
            f.slow_type('Playing a clip')
            f.play('intro')
            f.slow_type('You somehow survive')
            time.sleep(2)
            f.play('intro 2')
            f.audioplayer('scene-1')
            for i in range(14,20):
                f.slow_type(story1[i])
            print()
        else:
            f.slow_type('\nYou feel that going to your battalion is not safe and you venture alone\n')
            f.slow_type('By mistake you step on a mine\n')
            f.slow_type('YOU DIE!!\n',0.25)
            f.slow_type('THE END',0.25)
            sys.exit()
    records.write('s1')
    print()
    f.slow_type('.....',1)
    f.clearscreen()
    return

story2 = story[45:84]

def s2():
    f.slow_type('Playing a clip')
    f.play('portal')
    f.audioplayer('scene-2')
    global story2
    global records
    for i in range(0,3):
        f.slow_type(story2[i])
    move=''
    count=0
    move = input('What will you do?\n')
    while ('look' not in move) and ('explore' not in move):         
        if 'up' in move or 'down' in move or 'left' in move or 'right' in move:
            print('\nYour afraid to move and have no energy left\n')
        elif 'exit' in move:
            f.slow_type('You are exiting the game ;)')
            sys.exit()
        else:
            print('\nI can\'t do that')
        count=count+1
        if count>4:
            print('*Try looking around*')
        move = input('\nWhat will you do?\n')
    f.slow_type('Playing a clip')
    f.play('new world')
    f.audioplayer('scene-2')
    for i in range(3,6):
        f.slow_type(story2[i])
    time.sleep(2)
    print('1. Do you want to try to find shelter \nor\n2. You go on looking around the town')
    choice=input()
    if '1' in choice or 'shelter' in choice:
        f.slow_type(story2[14])
        f.slow_type(story2[15])
        print('Enter the building')
        c=input()
        if 'y' in c: 
            for i in range(16,25):
                f.slow_type(story2[i])
        else:
            print('You hear some strange sounds\nHence decide its best to move in')
            for i in range(16,25):
                f.slow_type(story2[i])
    else: 
        for i in range(27,31):
            f.slow_type(story2[i])
        print('How will you get in??')
        print('*Hint you have your gun with you*')
        move=input()
        while 'gun' not in move:
            print('Can\'t do that')
            move=input('Think of a solution:-\n')    
        for i in range(31,39):
            f.slow_type(story2[i])    
    print('What will you do??')
    f.slow_type('...',1)
    records.write('s2')
    f.clearscreen()
    return

story3 = story[93:119]

def s3():
    f.slow_type('Playing a clip')
    f.play('first shoot')
    f.audioplayer('scene-3')
    global story3
    global records
    for i in range(0,3):
        f.slow_type(story3[i])
    print('\nDo you want to continue??\n')
    move=input()
    if 'y' in move:
        f.slow_type('\nYou evetually run out of ammo\n')
        f.slow_type('The aliens kill you\n')
        f.slow_type('Playing a clip')
        f.play('death outside')
        time.sleep(2)
        f.slow_type('YOU DIE!!\n',0.3)
        f.slow_type('THE END\n')
        sys.exit()
    else:
        for i in range(3,10):
            f.slow_type(story3[i])
    print('\nYou have a gut feeling\n')
    f.slow_type('Do you want to:-')
    print('\n1. Try to go out  \n2. stay in the hospital')
    move=input()
    if 'stay' in move or '2' in move:
        for i in range(20,25):
            f.slow_type(story3[i])
        f.slow_type('Playing a clip')
        f.play('death in house')
        time.sleep(2)
        f.slow_type('THE END',0.3)
        sys.exit()
        
    else:
        f.slow_type('You finally decide to make an effort to find your fellow mate\'s')
    records.write('s3')
    f.slow_type('....',1)
    f.clearscreen()
    return

story4 = story[121:169]

def s4():
    f.audioplayer('scene-4')
    global story4
    global records
    for i in range(0,6):
        f.slow_type(story4[i])
    f.slow_type('...  \nAn idea strikes you')
    print('Do you want to try a different delicacy?')
    move=input()
    if 'no' in move:
        f.slow_type('Like the gentlemen you are')
        f.slow_type('You feel eating something alien is not good for now')
        f.slow_type('You just continue going through town')
    else:
        for i in range(13,16):
            f.slow_type(story4[i])
    for i in range(21,24):
        f.slow_type(story4[i])
    move=input('\nDo you want to reload?\n\n')
    if 'y' in move:
        f.slow_type('\nYou fill your ammo and then you look around the place.\n')
    for i in range(25,33):
        f.slow_type(story4[i])
    print('Seth appears to be on the floor')
    print('1.	Scare him and shoot few blanks to make sure he is still you buddy Seth and interrogate him\
    \nor\
	\n2.	Put down your weapon and then help him up')
    move=input('\nWhat do you want to do??\n')
    if '1' in move or 'shoot' in move or 'interrogate' in move:
        for i in range(39,43):
            f.slow_type(story4[i])
    else:
        for i in range(45,48):
            f.slow_type(story4[i])
    f.slow_type('Playing a clip')
    f.play('rescue scene')
    records.write('s4')
    f.slow_type('....',1)
    f.clearscreen()
    return

story5 = story[170:210]

def s5():
    f.audioplayer('scene-5')
    global story5
    global records
    for i in range(0,9):
        f.slow_type(story5[i])
    f.slow_type('playing a clip')
    f.play('treasure')
    f.audioplayer('scene-5')
    for i in range(9,11):
        f.slow_type(story5[i])
    print('\nYou are now against your friend')
    print('\nNote:- Seth is a combat veteran he is very much skilled than you')
    print('\nIt would be adivicable not to fight him')
    f.slow_type('....')
    f.slow_type('What do you want to do??')
    print('1. Take him down and attack him before he kills you\
    \nor\
    \n2. Put down your weapon and surrender') 
    move=input()
    if '1' in move or 'take' in move or 'kill' in move:
        f.slow_type('you pull his weapon from him but in the battle between you and your best pal.')
        f.slow_type('Both of you get engaged in a fist fight.')
        shot=0
        f.slow_type('Try to use all type of attacks!!')
        while shot!=3:
            move=input('\nWhat do you want to do?\n')
            if 'punch'  in move:
                print('\nSeth defends himself\n')
                f.slow_type('Seth punches you back, Your try to defend but he hits you hard\n')
                shot=shot +1
            elif  'gun' in move:
                print('\nYou don\'t have your gun\n')
                f.slow_type('Seth hits you\n')
                shot=shot+1
            else:
                print('\nSeth outsmarts you\n')
                f.slow_type('Seth hits you back\n')
                shot=shot+1
        for i in range(21,26):
            f.slow_type(story5[i])
        f.slow_type('Seth kills you')
        f.slow_type('THE END',0.5)
        sys.exit()
    else:
        for i in range(29,33):
            f.slow_type(story5[i])  
        f.slow_type('Playing a clip')
        f.play('Seth opens treasure')  
        f.audioplayer('scene-5')
        f.slow_type('\nYou are in shock what do you want to do?\n')
        print('Fight or Run\n')
        choice=input()
        if 'run' in choice:
            f.slow_type('\nYou try to outsmart him and run away but he eventually catches up')
            f.slow_type('\nHe tears your limbs and starts feeding on you as your alive')
            f.slow_type('\nTHE END')
            sys.exit()
        else:
            for i in range(33,40):
                f.slow_type(story5[i])        
    records.write('s5')
    f.slow_type('....',1)
    f.clearscreen()
    return

story6 = story[211:254]

def s6():
    f.slow_type('Playing a clip')
    f.play('portal')
    f.audioplayer('scene-6')
    global story6
    global records
    for i in range(0,9):
        f.slow_type(story6[i])
    print('\nYour are in the enemies BASE!!')
    time.sleep(2)
    print('\n1.	You slit the nurses throat and then make an escape\
    \nor\
    \n2.	You  try to talk to the nurse and understand the situation')
    move=input()
    if '1' in move or 'slit' in move:
        for i in range(15,17):
            f.slow_type(story6[i])
    else:
        for i in range(19,22):
            f.slow_type(story6[i])
    for i in range(23,26):
        f.slow_type(story6[i])
    move=input('Do you want to choose the \nFront entrance\nor\nBack entrance\n\n')
    if 'front' in move or 'Front' in move:
        f.slow_type('A group of guards see you ,They start firing at you')
        f.slow_type('Your arm gets blowen off\nYou are mortally wounded')
        f.slow_type('You DIE',0.5)
        f.slow_type('THE END',0.5)
        sys.exit()
    else:
        for i in range(26,35):
            f.slow_type(story6[i])
    print('Return back to your base \nor\nTry to stop them')
    move=input()
    if 'stop' in move:
        f.slow_type('\nYou try to stop them')
        f.slow_type('\nYou needed a crew to take them out\n')
        for i in range(37,41):
            f.slow_type(story6[i])
    else:
        f.slow_type('\nYou return back to your base, to call your crew\n')
        for i in range(37,41):
            f.slow_type(story6[i])
    f.slow_type(story6[42],0.4)
    f.slow_type('Playing a clip')
    f.play('ending scene')
    f.audioplayer('scene-6')
    f.slow_type('\nThanks for playing')
    f.slow_type('\nSOLDIER 0F FORTUNE',0.3)
    f.slow_type('\nHope to see you again!!')
    records.write('')
    f.slow_type('....',1)
    f.clearscreen()
    return


