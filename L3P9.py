high = 100
low = 0
guess = 0
epsilon = 1
answer = ''
print "Please think of a number between ", low," and ", high

while True:
    guess = (high + low) / 2
    s = 'Is your secret number ' + str(guess) + '?'
    print s
    answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == 'h':
        high = guess
    elif answer == 'l':
        low = guess
    elif answer == 'c':
        break
    else:
        print "that is not an option"
print "Game over.  Your secret number was: %r" % guess
