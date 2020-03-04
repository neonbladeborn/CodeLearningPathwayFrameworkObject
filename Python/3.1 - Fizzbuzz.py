# The starting and ending values for running the fizzbuzz loop through
start = 0
end = 100

# the variables to be used for returning fizz and buzz
fizzVar = 3
buzzVar = 4

#start of loop
for i in range (start, end):
	
	#initialising the tracker that bridges the gap between identifying and printing fizzbuzz
	fizzBuzzTracker = 0

	# incrementing based on which of the fizz and buzz were identified, inspired from binary tracking
	if (i / fizzVar) == int(i / fizzVar):
		fizzBuzzTracker + 1
	if (i / buzzVar) == int(i / buzzVar):
		fizzBuzzTracker + 2

	# prints fizz buzz based on the value of the fizzbuzztracker
	if (fizzBuzzTracker == 0):
		print("the number is ",i," ---")
	if (fizzBuzzTracker == 1):
		print("the number is ",i," Fizz")
	if (fizzBuzzTracker == 2):
		print("the number is ",i," Buzz")
	if (fizzBuzzTracker == 3):
		print("the number is ",i," FizzBuzz")