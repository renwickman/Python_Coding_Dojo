

print("Hello World")


name = "Anthony Renwick"
print("Hello", name,"!")
print("Hello"+ " " +name+"!")

name=42
print("Hello",name,"!")
print("Hello" + " " + str(name) + "!")

fave_food1 = "ice cream"
fave_food2 = "pizza"
print("My favorite food is {} and {}".format(fave_food1, fave_food2))
print(f"My favorite food is {fave_food1} and {fave_food2}.")

name = "Anthony Renwick"
print(str.upper(name))
print(str.lower(name))
print(str.isalpha(name))
print(str.split(name, " "))
print(str.count(name, "n"))
print("_".join(name))
print(str.endswith(name, "Renwick"))

#string.upper(): returns a copy of the string with all the characters in uppercase.

#string.lower(): returns a copy of the string with all the characters in lowercase.

#string.count(substring): returns number of occurrences of substring in string.

#string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.

#string.find(substring): returns the index of the start of the first occurrence of substring within string.

#string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.

#string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.

#string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.