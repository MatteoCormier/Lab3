# First Function
#We made a variable called "thing" and s will be an input for both an intger and string
thing = [(s) for s in input("Input numbers and integers with a space in between the two\n").split()]

#we need to then split function "thing" with...
def split (thing):
  #Define words variable
  words = []
  #Define numbers variable
  numbers = []
#We then need to find i in "thing"
  for i in (thing):
    #If the variable i isdigit function it will be true
    if i.isdigit() == True:
      #numbers get added to the list (i) or...
      numbers.append(i)
    else:
      #words get added to the list (i)
      words.append(i)
  #Then it all returns each of the words and the numbers
  return words, numbers

#Finally it just prints and splits our function "split(thing)"
print(split(thing))

def sort(numbers):
  list2 = []
  
# Second Function

a, b = split(thing)
b = [int(j) for j in b]

def second(b):
  final = []
  order = []
  order = sorted(b[1::2], reverse = True)
  del b[1::2]
  final = [None] * (len(b) + len(order))
  final[::2] = b
  final[1::2] = order
  return final

print(second(thing))