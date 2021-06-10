# First Function
#We made a variable called "thing" and s will be an input for both an intger and string
thing = [(s) for s in input("Input numbers and integers with a space in between the two\n").split()]

#we need to then split function "thing" with...
def split (thing):
  #Words with brackets
  words = []
  #Numbers with brackets 
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

# Second Function

