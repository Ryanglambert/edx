set x = 4
    range(x) = 0,1,2,3
        j0
            i0
                print i in range(x) >>> print i in (0,1,2,3)
                set x = 2 >>> x was 4 up until now
            i1
                print i in range(x) >>> print i in (0,1)
                set x = 2
            i2
                print i in range(x) >>> print i in (0,1)
                set x = 2
            i3
                print i in range(x) >>> print i in (0,1)
                set x = 2
        j1
            i0
                print i in range(x) >>> print i in (0,1)
                set x = 2
            i1
                print i in range(x) >>> print i in (0,1)
                set x = 2
    
        j2
            i0
                print i in range(x) >>> print i in (0,1)
                set x = 2
            i1
                print i in range(x) >>> print i in (0,1)
                set x = 2
        j3
            i0
                print i in range(x) >>> print i in (0,1)
                set x = 2
            i1
                print i in range(x) >>> print i in (0,1)
                set x = 2
    
