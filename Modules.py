import convertors

print(convertors.kg_to_g(5.665))
print(convertors.g_to_kg(5665))
# The above code imports the convertors module and uses its functions to convert between kilograms and grams.

from convertors import kg_to_lbs

a  = kg_to_lbs(100)
print(a)
# The above code imports the kg_to_lbs function from the convertor module and uses it to convert 100 kilograms to pounds.

from utils import find_max

n = []
e = int(input("How many elements do you want to enter: "))
print("Enter the number of elements: ")
for i in range(e):
    b  = int(input())
    n.append(b)

print("The List: ", n)
print("The maximum number is: ", find_max(n))

import utils

a = utils.find_min(n)
print("The minimum number is: ", a)
# The above code imports the find_max function from the utils module and uses it to find the maximum number in a list of user-inputted numbers.