x = raw_input('x')
y = raw_input('y')
z = raw_input('z')



# is x the smallest?

print " x = %r y = %r z = %r" % (x,y,z)
if x < y and x < z and x % 2 != 0:
    print 'x is the least odd number'
# x is not the smallest, so is y the smallest?
elif y < z and y % 2 != 0:
    print 'y is the least odd number'
elif z % 2 != 0:
    print 'z is the smallest odd number'
else:
    print ' there are no odd numbers'

