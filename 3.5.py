#Newton-Raphson for square root
#find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
y = 46.0
numGuesses = 0
guess = y/2.0
while abs(guess*guess -y) >= epsilon:
    guess = guess - (((guess**2)-y)/(2*guess))
    numGuesses += 1
    print numGuesses
print 'Square root of', y, 'is about', guess

print "Newton-Raphson Guesses = ", numGuesses

NRGuess = numGuesses

x = y
epsilon = 0.01
step = epsilon**2
numGuesses = 0 
low = 0.0 
high = max(1.0,x)
ans = 0.0 
while abs(ans**2 -x) >= epsilon:
    print 'low is = ', low 
    print 'high is = ', high
    numGuesses += 1
    print numGuesses
    if ans**2 < x:
        low = ans 
    else:
        high = ans 
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of' ,x
print "bisection guesses = ", numGuesses
print "Newton-Raphson Guesses = ", NRGuess
difference = (numGuesses - NRGuess)/float(numGuesses)*100

print "how much better is Newton-Raphson than bisection?  %r%%"  % difference
