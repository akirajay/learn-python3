#!/usr/bin/env python3
#Filename:if.py

number=23
guss=int(input('Enter an integer'))

if guss==number:
    print ('Con,you guessed it')
elif guss < number:
    print ('No,it is a little higher than that')
else:
    print ('No,it is a little lower than that')
print ('Done')
