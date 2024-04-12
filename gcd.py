# a = b * q + r
# 420 = 66 * 6 + 24, a = 420, b = 66, r = 24
# 66 = 24 * 2 + 18, a = 66, b = 24, r = 18
# 第一行的 b -> 第二行的 a , 第一行的 r -> 第二行的 b 

#法一
def gcd(a, b):
    while b != 0:
        r = a % b 
        a = b
        b = r

    return a

print(gcd(420,66))
print(gcd(560,340))
print(gcd(7544,115))

#法二：較為直觀
def gcd2(a, b):
    if(b == 0):
        return a
    else:
        return gcd2(b, a % b)

print(gcd(420,66))
print(gcd(560,340))
print(gcd(7544,115))