for i in range (0, 30):
	fizz = "false"
	buzz = "false"

	if (i / 4) == int(i / 4):
		fizz = "true"
	if (i / 3) == int(i / 3):
		buzz = "true"

	if (fizz == "false" and buzz == "false"):
		print("the number is ",i," ---")
	if (fizz == "true" and buzz == "false"):
		print("the number is ",i," Fizz")
	if (fizz == "false" and buzz == "true"):
		print("the number is ",i," Buzz")
	if (fizz == "true" and buzz == "true"):
		print("the number is ",i," FizzBuzz")