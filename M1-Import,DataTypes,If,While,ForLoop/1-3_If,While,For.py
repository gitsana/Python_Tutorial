

# else-if statement
x = 10
if(x > 30):
	print ('x is greater than 30')
elif (x < 20):
	print('x is less than 20')
else:
	print ('x is between 20 and 50')



# for loop
for i in range(10):
	print(i)



# while loop - use Ctrl + C for keyboard interrupt if you get into an infinite loop
x = 5
while (x != 0):
	print(x)
	x -= 1

# keep entering inputs until it breaks out of loop
while True:
	response = input()
	if int(response) == 7:	# cast to int bc originally inputs string
		print('Your response is 7. Breaking out of loop.')
		break

