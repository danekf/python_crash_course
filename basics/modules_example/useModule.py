
#import entire module
import converters
print(converters.lbs_to_kg_(180))

#can also import specific functions
from converters import kg_to_lbs
print(kg_to_lbs(81))