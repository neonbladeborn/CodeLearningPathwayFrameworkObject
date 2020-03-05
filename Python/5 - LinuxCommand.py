import os

commandList = open("5.1 - commandList", "r") # open the file that contains all the commands
commandArray = [] # initialise the array that holds all the commands

#for all the lines in the list add them to the array
for line in commandList: 
	commandArray.append(line) 

#runs each command in the array
for x in commandArray:
	os.system(x)