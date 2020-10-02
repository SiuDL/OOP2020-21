#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        print("Hello, this is my second OOP lab.")

        # print only first and last of the sentence:
        print(message[0])
        print(message[-1])

        # use slice notation:
        statement = "message"
        print(statement[:1])
        print(statement[6:7])

        # escaping a character:
        print("he said \"that\'s fantastic\"!")

        # find all a's in the input word and count how many there are:
        print(statement.find('a'))
        print(statement.count('a'))

        # replace all occurences of the character a with the - sign
        print("This is another tribute to a vergil".replace('a','-'))

        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        print("This is another tribute to a vergil".replace('a','-',1))


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        myList = (list(message.split()))
        print(myList)

        # append a new element to the list and print:
        myList.append(" yes")
        print(myList)

        # remove from the list in 3 ways:
        del myList[3]
        print(myList)
        myList.remove(' yes')
        print(myList)

        # check if the word cake is in your input list:
        print("cake" in myList)

        # reverse the items in the list and print:


        # reverse the list with the slicing trick:


        # print the list 3 times by using multiplication:



tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
