unsortedList = open("4.1 - unsortedList", "r")
arraylist = []

for line in unsortedList: #for all the lines in the list document
	arraylist.append(line) #it adds that line to the end of the array

sortedList = open("4.2 - sortedList", "w") 
sortedList.seek(0) # goes to start of file
sortedList.truncate() # deletes all data

#loop to go through the array enough times to bubble sort
for p in range(len(arraylist)):
	for i in range(len(arraylist) - 1): #not overshooting the array
		if (int(arraylist[i]) > int(arraylist[i + 1])): #converting to int for sorting, remove int for alphabetical sorting 
			#sorting 2 elements in array
			temp = arraylist[i+1]
			arraylist[i+1] = arraylist[i]
			arraylist[i] = temp

for x in arraylist:
	sortedList.write(x) #writes all the elements into the array
