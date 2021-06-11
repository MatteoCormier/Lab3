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

#just prints out what the program is doing
print("Your list of words and numbers is:\n")
#Finally it just prints and splits our function "split(thing)"
print(split(thing))
  
# Second Function

#Make variable a and b and spilt using "thing" like the thing before
a, b = split(thing)

#only look at b so that it doesnt try to sort the strings
b = [int(j) for j in b]
#Define the second for b
def second(b):
  #Define final variable
  final = []
  #Define order variable
  order = []
  #Use the order to sort b::2 and reverse true
  
  order = sorted(b[1::2], reverse = True)
  #del b1::2 like before exepct no reverse true
  del b[1::2]
  #Final has to equal none for lenb to + len order
  final = [None] * (len(b) + len(order))
  #Final will use the thing to equal to b
  final[::2] = b
  #final also this is for order
  final[1::2] = order
  #It will final return final
  return final
  
#And this will just print the message that will be listed here
print("Here are your numbers where every second number is put into a descending order:\n")
#This is how you print the numbers
print(second(thing))