unsortedList = open("4.1 - unsortedList", "r")
arraylist = []

for line in unsortedList:
	arraylist.append(line)

sortedList = open("4.2 - sortedList", "w")
sortedList.seek(0) # goes to start of file
sortedList.truncate() # deletes all data

for p in range(len(arraylist)):
	for i in range(len(arraylist) - 1):
		if (arraylist[i] > arraylist[i + 1]):
			temp = arraylist[i+1]
			arraylist[i+1] = arraylist[i]
			arraylist[i] = temp





for x in arraylist:
	sortedList.write(x)




