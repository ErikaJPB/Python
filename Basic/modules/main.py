# Import a module

import mymodule

print(mymodule.generate_full_name('Erika', 'Pineda'))


# Import functions from a module

from mymodule import generate_full_name, sum_two_nums

print(generate_full_name("Erika", "Pineda"))
print(sum_two_nums(1, 9))


# Import functions from a module and renaming

from mymodule import generate_full_name as fullname, sum_two_nums as total

print(fullname("Erika", "Pineda"))
print(total(1, 9))