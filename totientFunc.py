def totient(n):
    num = n
    s= set()
    p = 2
    while(p<=n):
        if(n%p == 0):
            s.add(p)
            n = n/p
        else:
             p +=1
    print(s)

    v1 = 1
    v2 = 1
    for item in s:
        v1 = v1 *(item -1)
        v2 = v2 *(item)
    
    print(num*v1/v2)

totient(120)