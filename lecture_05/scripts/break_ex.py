# BREAK STATEMENT EXAMPLE

# Run this script from terminal or anaconda prompt
# after activating your conda environment

# To run in debug mode run as:
# python -m ipdb break_ex.py 

print('\nbreak statement')
letters = ['a', 'b', 'c']
numbers = [5, 7, 9, 10, 15]
for char in letters:                         # outer loop
    for number in numbers:  # inner loop; enumerate gives (index, value) tuples (see help)
        if number % 2 == 0:
            break
        print(char, number)



