# Pt2-AoCDay2.py
# 2018 Advent of Code
# Day 2
# Part 2

"""

--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)

Your puzzle answer was jbbenqtlaxhivmwyscjukztdp.

"""
from __future__ import print_function

# define an empty list
boxIDs = []

accum = 0	# Accumulated sum

def dumpSame(string1,string2):
	"""dumpSame - make a string from the same digits
	"""
	#print 'Dump the same chars between strings'
	newString = ''
	charOffset = 0
	for char in string1:
		if char == string2[charOffset]:
			newString += char
		charOffset += 1
	return newString

def countDiffs(string1,string2):
	"""countDiffs - count the number of different chars in a string
	"""
	#print 'counting differences between strings'
	diffCount = 0
	charOffset = 0
	for char in string1:
		if char != string2[charOffset]:
			diffCount += 1
		charOffset += 1
	return diffCount

# open file and read the content into an accumulated sum
with open('input.txt', 'r') as filehandle:  
	for line in filehandle:
		boxIDs.append(line.strip('\n\r'))
#print boxIDs

string2Offset = 0
for string1 in boxIDs:
	string2Offset += 1
	for string2 in boxIDs[string2Offset:]:
		if countDiffs(string1,string2) == 1:
			print('String1',string1)
			print('String2',string2)
			print('Checksum',(dumpSame(string1,string2)))