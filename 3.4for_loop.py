x = 24
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
