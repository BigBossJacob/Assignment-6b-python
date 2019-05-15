itt = int(input("Enter a number: "))+1

logic = -1

answer = 0

for math in range(1, itt, 1):
	logic = logic*-1
	answer = answer + 4/(2*math-1)*logic

if answer > 0:
	print("The Answer Is: ", answer)
else:
	print("Invalid Input")