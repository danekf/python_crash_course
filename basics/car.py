exit = False
previous_command = ''

while exit != True:
  
  command = input("tell me what to do ")
  if command == 'start' and previous_command == 'start':
    print('Your car is already started, go drive.')
  elif command == 'start' :
    print('Car started, go drive homeboy')
  elif command == 'stop' and previous_command == 'stop':
    print('Your car is already stopped, maybe you should start it, so you can stop it.')
  elif  command == 'stop':
    print('Car is shut down. No driving for now.')
  elif command == 'quit':
    print('Exiting...')
    exit = True
  else:
    print("I am not yet sentient enough to understand that command. Please come back after my day one patch is complete.")
  
  previous_command = command

print('I hope you enjoyed Keying your car.')