"""Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs
control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all
uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively."""


def main():
    grocery_list = []
    while True:
        try:
            entry = str(input()).lower()
            grocery_list.append(entry)
        except EOFError:
            break

    grocery_list = sorted(grocery_list)
    final_list = {}
    for i in grocery_list:
        if i not in final_list:
            final_list[i] = 1
        else:
            final_list[i] += 1

    for c in final_list:
        print(final_list[c], c.upper())


main()

"""This was the output of the build-in 'check50' function"""
# :) grocery.py exists
# :) input of EOF halts program
# :) input of "apple" and "banana" yields "1 APPLE 1 BANANA"
# :) input of "strawberry" and "strawberry" yields "2 STRAWBERRY"
# :) input of "mango", "sugar", and "mango" yields "2 MANGO 1 SUGAR"
# :) input of "tortilla" and "sweet potato" yields "1 SWEET POTATO 1 TORTILLA"
