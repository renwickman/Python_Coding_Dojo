def countdown(num):
  for x in range(num, 0, -1):
    print (x)

# countdown(num)

def print_and_return(arr):
  print (arr[0])
  return arr[1]

def first_plus_length(arr):
    return arr[0] + len(arr)

first_plus_length([0,1,3,4,5,9])

def greater(arr):
    new_arr = []
    if len(arr) == 0:
        return False
    for i in arr:
        if arr[2] => arr[i]:
            new_arr.append(arr[i])
    print(new_arr)
    print(len(new_arr))

def length_value(num_1, num_2):
    new_arr = []
        if num1 == num2:
            print('Numbers cant be equal')
        for i in range (0, num_1):
            new_arr.append(num_2)
    return new_arr