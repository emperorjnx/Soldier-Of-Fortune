with open('records.txt','r') as records:
    record = records.readline()
import functions as f
import story as s
import sys
import time


f.slow_type('WELCOME TO SOLDIER OF FORTUNE\n',0.3)

with open('Scenario.txt','r') as scene:
    story = scene.readlines()

f.slow_type('Do you want to view the help section?')
choice=input()
if 'ok' in choice or 'y' in choice:
    print()
    with open('help.txt','r') as help:
        h=help.readlines()
        for i in h:
            f.slow_type(i)
else:
    f.slow_type('\n Your wish \n')

f.slow_type('\n\nBEGIN THE GAME?\n\n',0.3)
choice=input()
if 'y' in choice:
    f.slow_type('\nCool then lets begin\n')
    f.clearscreen()
else:
    f.slow_type('Ok then see you next time')
    sys.exit()

data=''

if record.isalnum() and record.startswith('s'):
    print('\nOld data save found want to continue\n')
    move=input()
    if 'no' in move:
        f.clearscreen()
        for i in range(0,4):
            f.slow_type(story[i])
        print()
        time.sleep(2)
        for i in range(5,11):
            f.slow_type(story[i])
        print()
        f.slow_type('\nStarting the game\n')
        f.slow_type(story[14])
        print()
    else:
        data=record
        f.clearscreen()
else:
    for i in range(0,4):
        f.slow_type(story[i])
    print()
    time.sleep(2)
    for i in range(5,11):
        f.slow_type(story[i])
    print()
    f.slow_type('\nStarting the game\n')
    f.slow_type(story[14])
    print()

while data!='s6':
    if data=='':
        s.s1()
        print('\nWhat do you want to do??')
        print('1.  Enter the portal\
        \nor\
        \n2.	Go back in search of what happened in your field')
        choice=input('1 or 2\n')
        if '1' in choice:
            f.slow_type(story[42])
        else:
            f.slow_type(story[43])
        data='s1'
    if data=='s1':
        s.s2()
        print('\nDo you want to:-')
        print('1.	Talk to him and ask what he wants\
        \nor\
        \n2.	Shoot him down\n')
        choice=input('1 or 2\n')
        if '1' in choice:
            f.slow_type('He might have looked slightly human but he didn\'t want much.\
            \nOther than your dead body so when you see him running towards you shoot him down.')
        data='s2'
    if data=='s2':
        s.s3()
        data='s3'
    if data=='s3':
        s.s4()
        data='s4'
    if data=='s4':
        s.s5()
        data='s5'
    if records.read()=='s5':
        s.s6()
        data='s6'

f.slow_type('THANKS FOR PLAYING')