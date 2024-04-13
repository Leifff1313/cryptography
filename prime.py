# check if n is prime or not, if yes, return True 
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    s = 3 
    while(s < n):
        if(n % s == 0):
            return False
        s +=1
    return True

print(isPrime(50))
print(isPrime(97))
