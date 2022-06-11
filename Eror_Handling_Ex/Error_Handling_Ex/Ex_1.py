numbers_dictionary = {}

line = input('Please enter string number: ')
while line != "Search":
    try:
        number_as_string = line
        number = int(input('Please enter integer number: '))
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable must be an integer")
    line = input('Please enter string number: ')

line = input('Please enter string number: ')
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])

    except KeyError:
        print('Number dose not exist in dictionary')
    line = input('Please enter string number: ')

line = input('Please enter string number: ')
while line != "End":
    searched = line
    del numbers_dictionary[searched]
    line = input('Please enter string number: ')

print(numbers_dictionary)
