# PROBLEM 1
def return_a_variable():
	strAndNum = "Day" + str(1)
	myVariable = 10
	return myVariable
print(return_a_variable())


# PROBLEM 2
def ifStatement():
	myVariable = 50
	bool = True
	if (myVariable == 99999 and False):
		myVariable -= 1
		print("To infinity")
	elif (myVariable == 50):
		myVariable += 1
		print("And beyond")
	else:
		print("YOU. ARE. A. TOY!")
	return myVariable
print(ifStatement())

# PROBLEM 3
def forLoop(arr):
	arr.pop()
	arr.append(6)
	for i in range(0, len(arr), 1):
		print(arr[i])
forLoop([3,7,2,9])


arr = [{"name": "Fred"}, {"name": "Daphne"}]

for x in arr:
  print(x['name'])

for y in range(0, len(arr), 1):
  print(arr[y]['name'])

# print(arr[y]) == print(x)

arr2 = [9, 4, 6]

for x in range(0, len(arr2), 1):
  print(arr2[x])