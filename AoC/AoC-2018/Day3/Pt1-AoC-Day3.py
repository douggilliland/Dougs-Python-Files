# Pt1-AoCDay3.py
# 2018 Advent of Code
# Day 3
# Part 1
# https://adventofcode.com/2018/day/3

import time
import re

"""
--- Day 3: No Matter How You Slice It ---

The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:
  - The number of inches between the left edge of the fabric and the left edge of the rectangle.
  - The number of inches between the top edge of the fabric and the top edge of the rectangle.
  - The width of the rectangle in inches.
  - The height of the rectangle in inches.

A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:
...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........

The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2

Visually, these claim the following areas:
........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........

The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?

Your puzzle answer was 567.

"""

def checkOverlap(card1,card2):
	"""checkOverlap - Check the two cards for overlap
	cardX format [cardNumber,startX,startY,endX,endY]
	
	Example which overlaps
		card1 = [1, 1, 3, 4, 6]
		card2 = [2, 3, 1, 6, 4]
	
	:returns: True if the cards overlap, False if there's no overlap
	"""
	#print 'checkOverlap: checking card',card1,'vs card',card2
	leftX = 0
	lowerY = 1
	rightX = 2
	upperY = 3
	if card1[leftX] > card2[rightX]:
		return False
	elif card1[rightX] < card2[leftX]:
		return False
	elif card1[lowerY] > card2[upperY]:
		return False
	elif card1[upperY] < card2[lowerY]:
		return False
	else:
		#print 'overlaps'
		return True
	
def parseLine(claimCardRaw):
	"""parseLine example line #1 @ 7,589: 24x11
	:returns: [startX,startY,endX,endY]
	"""
	#print 'claimCardRaw',claimCardRaw
	inputLineList = re.split('[\D]+',claimCardRaw[1:])		# make this really easy
	#print 'inputLineList',inputLineList
	accumCardNumber = int(inputLineList[0])
	accumStartX = int(inputLineList[1])
	accumStartY = int(inputLineList[2])
	accumSizeX = int(inputLineList[3])
	accumSizeY = int(inputLineList[4])
	listToReturn = []
	listToReturn.append(accumStartX)
	listToReturn.append(accumStartY)
	listToReturn.append(accumStartX + accumSizeX - 1)
	listToReturn.append(accumStartY + accumSizeY - 1)
	#print 'list',listToReturn
	return listToReturn

def isCardInArea(xValue,yValue,checkingCard):
	"""isCardInArea - check to see if the current card is at a particular point
	:returns: True if the x,y point is in the card
	"""
	cardStartX = checkingCard[0]
	cardStartY = checkingCard[1]
	cardEndX = checkingCard[2]
	cardEndY = checkingCard[3]
	if xValue < cardStartX:
		return False
	if xValue > cardEndX:
		return False
	if yValue < cardStartY:
		return False
	if yValue > cardEndY:
		return False
	#print 'Card',checkingCard,'is at point (',xValue,',',yValue,')'
	return True

# define an empty list
claimCards = []
overlappingCards = 0	# Total of overlapping cards

print 'Reading in file',time.strftime('%X %x %Z')

# open file and read the content into an accumulated sum
with open('input.txt', 'r') as filehandle:  
	for line in filehandle:
		claimCards.append(parseLine(line.strip('\n\r')))

#print 'claimCards',claimCards

overlappingCards = []
overlappingCardCount = 0
overlappingAreas = []
cardNumber2 = 0
print 'Getting list of overlapping areas',time.strftime('%X %x %Z')
for card1 in claimCards:
	cardNumber2 += 1
	for card2 in claimCards[cardNumber2:]:
		if checkOverlap(card1,card2) or checkOverlap(card2,card1):
			#print 'Card 1',card1, 
			#print 'overlaps Card 2',card2
			if card1 not in overlappingCards:
				overlappingCards.append(card1)
				overlappingCardCount += 1
			if card2 not in overlappingCards:
				overlappingCards.append(card2)
				overlappingCardCount += 1
			
		cardNumber2 != 1
#print 'Overlapping card count',overlappingCardCount
#print '\nList of overlapping cards',overlappingCards

# Cycle through all 1000x1000 locations to count how many times each cell is in a list

print 'Starting matrix check',time.strftime('%X %x %Z')
totalCellsWithMoreThanOne = 0
yValue = 0
while yValue < 1024:
	print '.',
	xValue = 0
	while xValue < 1024:
		cardCountInArea = 0
		for checkingCard in overlappingCards:
#			print 'checkingCard',checkingCard
			if isCardInArea(xValue,yValue,checkingCard):
				cardCountInArea += 1
		if cardCountInArea > 1:
			totalCellsWithMoreThanOne += 1
		xValue += 1
	yValue += 1
print '\nEnded',time.strftime('%X %x %Z')
print 'Total Cells With More Than One', totalCellsWithMoreThanOne
