"""In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted
with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The
bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”,
output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading
whitespace in the user’s greeting, and treat the user’s greeting case-insensitively."""


def main():
    greeting = str(input('What was the greeting?')).strip().lower()
    if greeting[:5] == 'hello':
        print('$0')
    elif greeting[:5] != 'hello' and greeting[0] == 'h':
        print('$20')
    else:
        print('$100')


main()

"""This was the output of the build-in 'check50' function"""
# :) bank.py exists
# :) input of "Hello" yields output of $0
# :) input of " Hello " yields output of $0
# :) input of "Hello, Newman" yields output of $0
# :) input of "How you doing?" yields output of $20
# :) input of "What's happening?" yields output of $100
# :) input of "What's up?" yields output of $100
