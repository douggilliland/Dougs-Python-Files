# Pt1-AoCDay4.py
# Pt1-AoCDay4.py
# 2018 Advent of Code
# Day 4
# Part 1
# https://adventofcode.com/2018/day/4

import time

"""
--- Day 4: Repose Record ---
You've sneaked into another supply closet - this time, it's across from the prototype suit manufacturing lab. You need to sneak inside and fix the issues with the suit, but there's a guard stationed outside the lab, so this is as close as you can safely get.

As you search the closet for anything that might help, you discover that you're not the first person to want to sneak in. Covering the walls, someone has spent an hour starting every midnight for the past few months secretly observing this guard post! They've been writing down the ID of the one guard on duty that night - the Elves seem to have decided that one guard was enough for the overnight shift - as well as when they fall asleep or wake up while at their post (your puzzle input).

For example, consider the following records, which have already been organized into chronological order:

[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
Timestamps are written using year-month-day hour:minute format. The guard falling asleep or waking up is always the one whose shift most recently started. Because all asleep/awake times are during the midnight hour (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those events.

Visually, these records show that the guards are asleep at these times:

Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01  #10  .....####################.....#########################.....
11-02  #99  ........................................##########..........
11-03  #10  ........................#####...............................
11-04  #99  ....................................##########..............
11-05  #99  .............................................##########.....
The columns are Date, which shows the month-day portion of the relevant day; ID, which shows the guard on duty that day; and Minute, which shows the minutes during which the guard was asleep within the midnight hour. (The Minute column's header shows the minute's ten's digit in the first row and the one's digit in the second row.) Awake is shown as ., and asleep is shown as #.

Note that guards count as asleep on the minute they fall asleep, and they count as awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.

If you can figure out the guard most likely to be asleep at a specific time, you might be able to trick that guard into working tonight so you can have the best chance of sneaking in. You have two strategies for choosing the best guard/minute combination.

Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas any other minute the guard was asleep was only seen on one day).

While this example listed the entries in chronological order, your entries are in the order you found them. You'll need to organize them before they can be analyzed.

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 10 * 24 = 240.)

Your puzzle answer was 95199.

"""

def readTextFileToList(fileName):
	"""
	"""
	textFile = []
	# open file and read the content into an accumulated sum
	#print 'Reading in file',time.strftime('%X %x %Z')
	with open(fileName, 'r') as filehandle:  
		for line in filehandle:
			textFile.append(line.strip('\n\r'))
		textFile.sort()
	return textFile

def filterInputLine(theLine):
	"""filterInputLine - Filter the input line based on replace and split of the original lines.
	Replace all spaces and other delimiters with commas into a single dimension list.
	Three example record types with columns
	[1518-11-01 23:58] Guard #99 begins shift
	[1518-11-02 00:40] falls asleep
	[1518-11-02 00:50] wakes up
	Changes first line to
	1518,11,01,23,58,Guard,99,begins,shift
	YYYY,MM,DD,HH,MM,Key,Opt1,Opt2
	0   ,1 ,2 ,3 ,4 ,5  ,6   ,7
	"""
	newRecord = theLine
	newRecord = newRecord.replace('[','')
	newRecord = newRecord.replace(']','')
	newRecord = newRecord.replace('-',',')
	newRecord = newRecord.replace(':',',')
	newRecord = newRecord.replace('#','')
	newRecord = newRecord.replace(' ',',')
	newRecord = newRecord.split(',')
	return newRecord
	
def parseGuardLog(guardLog):
	"""parseGuardLog - Turns three record types into single records remembering the guard number in case it is not changed
	[1518-11-01 23:58] Guard #99 begins shift
	[1518-11-02 00:40] falls asleep
	[1518-11-02 00:50] wakes up
	Turned by filterInputLine to be
	YYYY,MM,DD,HH,MM,Key,Opt1,d/c
	0   ,1 ,2 ,3 ,4 ,5  ,6   ,7
	Key is either Guard, falls or wakes
	Opt1 is Guard number when Key is Guard
	"""
	totalTimeAsleep = 0
	asleepTime = 0
	awakeTime = 0
	sleepLog = []
	for record in guardLog:
		newRecord = filterInputLine(record)
		#print 'newRecord',newRecord
		if (newRecord[5] == 'Guard'):
			guardNumber = int(newRecord[6])
		elif (newRecord[5] == 'falls'):
			asleepTime = int(newRecord[4])
		elif (newRecord[5] == 'wakes'):
			awakeTime = int(newRecord[4])
			totalTimeAsleep = awakeTime - asleepTime
			sleepLogLine = []
			sleepLogLine.append(guardNumber)
			sleepLogLine.append(asleepTime)
			sleepLogLine.append(awakeTime-1)
			sleepLogLine.append(totalTimeAsleep)
			sleepLog.append(sleepLogLine)
		else:
			print 'parseGuardLog: key error'
			exit()
	guardHoursList = sorted(sleepLog, key = lambda errs: errs[0])		# sort by length column
	return guardHoursList
	
def oldParseGuardLog(guardLog):
	"""
	012345678901234567890123456789
	[1518-11-01 23:58] Guard #99 begins shift
	[1518-11-02 00:40] falls asleep
	[1518-11-02 00:50] wakes up
	"""
	sleepLog = []
	guardNumber = 0
	totalTimeAsleep = 0
	asleepTime = 0
	awakeTime = 0
	#print 'parseGuardLog: parsing raw log',guardLog
	for record in guardLog:
		timeMins10s = ord(record[15]) - ord('0')
		timeMins1s = ord(record[16]) - ord('0')
		timeMins = 10*timeMins10s + timeMins1s
		#print 'time',timeMins,
		if record[19] == 'G':	# Guard record
			if record[25] != '#':	# verify record type is correct
				print 'error - expected a pound'
				exit()
			lineOff = 26
			if guardNumber != 0:
				totalTimeAsleep = 0	# reset the time
			guardNumber = 0
			while (record[lineOff] != ' '):
				guardNumber = guardNumber * 10
				guardNumber += ord(record[lineOff]) - ord('0')
				lineOff += 1
			hourworthOfZeros = [0] * 60
			#print 'guard',guardNumber
		elif record[19] == 'f':
			#print 'falls asleep at',timeMins,
			asleepTime = timeMins
		elif record[19] == 'w':
			#print 'wakes up at',timeMins,
			awakeTime = timeMins
			totalTimeAsleep += awakeTime - asleepTime
			sleepLogLine = []
			sleepLogLine.append(guardNumber)
			sleepLogLine.append(asleepTime)
			sleepLogLine.append(awakeTime-1)
			sleepLogLine.append(totalTimeAsleep)
			sleepLog.append(sleepLogLine)
			totalTimeAsleep = 0
			#print 'slept for',totalTimeAsleep
	#print 'sleepLog',sleepLog
	guardHoursList = sorted(sleepLog, key = lambda errs: errs[0])		# sort by length column
	#print guardHoursList
	return guardHoursList

def mostLikelyAsleepTime(selectedGuardHours):
	"""
	"""
	#print 'selectedGuardHours',selectedGuardHours
	minutesList = [0 for i in range(60)]
	for record in selectedGuardHours:
		startTime = record[0]
		endTime = record[1]
		time = startTime
		while(time <= endTime):
			minutesList[time] += 1
			time += 1
	#print 'minutesList',minutesList
	startTime = 0
	endTime = 59
	currentTime = 0
	maxCountNumber = minutesList[1];
	maxCountTime = 0
	while(currentTime <= endTime):
		#print 'time',currentTime,'count',minutesList[currentTime],'maxCountTime',maxCountTime
		if minutesList[currentTime] > maxCountNumber:
			maxCountNumber = minutesList[currentTime]
			maxCountTime = currentTime
			#print 'max at',currentTime
		currentTime += 1
	return maxCountTime

def maxHours(guardIDvsHours):
	"""
	"""
	maxHours = 0
	selGuard = []
	#print 'guardIDvsHours',guardIDvsHours
	for guardIDTotalHours in guardIDvsHours:
		#print 'guardID',guardIDTotalHours[0]
		#print 'total hrs',guardIDTotalHours[1]
		if guardIDTotalHours[1] > maxHours:
			maxHours = guardIDTotalHours[1]
			selGuard = guardIDTotalHours
	#print 'selGuard',selGuard
	return selGuard

def getHoursByGuardID(guardLog):
	"""
	input list is in format:
	[guardNumber, sleepStartTime, sleepEndTime, sleepTime]
	"""
	guardHours = {}
	
	for guardRecord in guardLog:
		#print 'processing guardRecord',guardRecord
		if guardRecord[0] in guardHours:
			#print '  record exists'
			#print 'hours before',guardHours[guardRecord[0]]
			guardHours[guardRecord[0]] = guardHours[guardRecord[0]] + guardRecord[3]
			#print 'hours after',guardHours[guardRecord[0]]
		else:
			#print '  new record guard number',guardRecord[0],
			#print 'guard hours',guardRecord[3]
			guardHours[guardRecord[0]] = guardRecord[3]
	
	#print 'guardHours',guardHours
	guardHoursList = []
	for key,value in guardHours.iteritems():
		temp = [key,value]
		guardHoursList.append(temp)
	#print 'guardHoursList',guardHoursList
	return guardHoursList

def extractGuardRecords(guardList,selectedGuardID):
	newList = []
	for record in guardList:
		if record[0] == selectedGuardID:
			newList.append(record[1:])
	#print 'newList',newList
	return newList

guardLog = readTextFileToList('input.txt')
guardList = parseGuardLog(guardLog)
guardIDvsHours = getHoursByGuardID(guardList)
maxHoursForAllGuards = maxHours(guardIDvsHours)
#print 'Total max hours [Guard ID, hours] =',maxHoursForAllGuards
print 'Guard with the most total hours =',maxHoursForAllGuards[0]
print 'Total hours', maxHoursForAllGuards[1]
timeRecords = extractGuardRecords(guardList,maxHoursForAllGuards[0])
criticalTime = mostLikelyAsleepTime(timeRecords)
#print 'Critical Time to do job',criticalTime
print 'PRODUCT=',maxHoursForAllGuards[0]*criticalTime