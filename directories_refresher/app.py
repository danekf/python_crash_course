from pathlib import Path

#relative path from file, blank is current dir
path = Path('ecommerce')

#will return true if the ecommerce directory exists in this location
print(path.exists())


#create a new dir, return none when complete without issues
path2 = Path('emails')
print(path2.mkdir())

#remove a dir
print(path2.rmdir())


#search dir given and show all .py files
for file in (path.glob('*.py')):
  print(file)
  
