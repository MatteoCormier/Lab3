# First Function
#We made a variable called "thing" and s will be an input for both an intgers and 
thing = [(s) for s in input("Input numbers and integers with a space in between the two\n").split()]

def split (thing):
  words = []
  numbers = []

  for i in (thing):
    if i.isdigit() == True:
      numbers.append(i)
    else:
      words.append(i)
  return words, numbers

print(split(thing))

def sort(numbers):
  list2 = []

# Second Function

