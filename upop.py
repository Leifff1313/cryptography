def primeFactor(n):
    ans =str(n)  + " = "
    p = 2
    while(p<=n):
        if(n%p == 0):
            ans += str(p) + "x"
            n = n/p
        else:
             p +=1

    print(ans[:len(ans)-1])

primeFactor(120)
primeFactor(1200)



