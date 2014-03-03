def isIn(s1,s2):
    count1 = 0
    count2 = 0
    for letter in s1:
        count1 += 1
        if letter in s2:
            return True
    for letter in s2:
        count2 += 1
        if letter in s1:
            return True

print isIn('hey','he')
