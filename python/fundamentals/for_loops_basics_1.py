for i in range (1, 151):
    print(i)

for x in range (0,1000,5):
    print(x)

def divisible ():
for b in range(1, 101, 1):
    if b%10 == 0:
      print("Coding Dojo")
    elif b%5 == 0:
      print("Coding")
    else:
      print(b)

sum = 0
for y in range (1, 500000,2):
    sum += y
    print(sum)

for a in range (2018, 1,-4):
    print(a)

def multiple(lowNum, highNum, mult):
    for d in range(lowNum, highNum, mult):
        print(d)
    if lowNum >= highNum:
      print("Wrong Order")
multiple(20,0,2)
    