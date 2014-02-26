x = int(raw_input('enter an integer'))
ans = 0
while ans**2 < abs(x):
    ans = ans + .01
else:
    if x < 0:
        ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)
#output two integers
    #root and pwr
#0 < pwr < 6 and root^pwr = int
