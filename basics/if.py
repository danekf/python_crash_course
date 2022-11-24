#example if program
#python closes if statements using indentation rather than any other formal break or closing brackets.

temp = 'wet'

if temp == 'hot':
  print("It's a hot day")
  #because the next line is in the same indent, it will execute, if it was further in, it would break the program with an "unexpected indent" error
  print("Drink plenty of water")
elif temp == 'cold':
  print("It's a cold day")
  print("Wear warm clothes")
else:
  print ("It's a", str(temp),"day.")

#because this line is indented further back, it is not part of the if statement, and will always be displayed
print("Enjoy your day")