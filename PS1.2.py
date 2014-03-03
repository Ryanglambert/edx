s = 'bobopedicbobomatic, bobberbobson'
bob_count = 0
bob = 'c'

def bobInString(s):
    ''' 
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if s in bob:
        return True
    else:
        return False

for bob in s:
    if bob in s:
        bob_count += 1
print "The total number of bob's is: ", bob_count    
