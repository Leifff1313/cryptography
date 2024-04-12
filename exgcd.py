#需要多看幾次，有點難...
def linear_combination(a,b):
    q, r = divmod(a,b) #a = bq + r
    print(f'a = {a}, b = {b}, q = {q}, r = {r}')

    if(r == 0):
        return (0,1)
    else:
        #x, y we got from linear_combination(b,r) are x2, y2
        x, y = linear_combination(b,r)
        return (y, x - q*y)

a = 486
b = 43
x,y = linear_combination(a, b)
print(f'{a}*{x} + {b}*{y} == {a*x+b*y}')