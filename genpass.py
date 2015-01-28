#!/usr/bin/python

# script to generate password whithout string: o, 0, O and I
# password structure (SECTION): small strings + numbers + big strings + small strings
# by lunaferie
# v1.1

# CONFIGURE:

section_length = 4

########################################

import sys
import random

numbers = []
smallstrings1 = []
smallstrings2 = []
bigstrings = []

for i in range(1, section_length + 1):
    first = random.randint(1,9)
    numbers.append(first)

for i in range(1, section_length + 1):
    second = random.choice("abcdefghijklmnprstuwxyz")
    smallstrings1.append(second)

for i in range(1, section_length + 1):
    second = random.choice("abcdefghijklmnprstuwxyz")
    smallstrings2.append(second)

for i in range(1, section_length + 1):
    third = random.choice("ABCDEFGHJKLMNPRSTUWXYZ")
    bigstrings.append(third)

password = smallstrings1 + numbers + bigstrings + smallstrings2

for i in password:
    print i,
    sys.stdout.write('')

print "\nYour password have" , len(password) , "characters"





