#new file for playing with on github :)

fruitList = ["apple","banana","pear","peach","kiwi","orange","grape","strawberry"]
counter = 0

def printStatement():
    print(fruit + " is the " + str(counter) + ending + " item in this list.")
    
for fruit in fruitList:
    counter = counter + 1
    if counter == 1:
        ending = "st"
        printStatement()
    if counter == 2:
        ending = "nd"
        printStatement()
    if counter == 3:
        ending = "rd"
        printStatement()
    if counter == 4 or counter == 5:
        ending = "th"
        printStatement()
#hiiiiiiii this is a test edit
