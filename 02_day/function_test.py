
def add_two_numbers(a,b):
    summ = a + b
    return summ
c = add_two_numbers(2,3)
print(c)

def area(r):
    ar = 3.14 * r * r
    return ar
d = area(10)
print(d)

def add_all_nums(*nums):
    summ = 0
    for num in nums:
        if type(num) != int:
            print('Error invalid input type - must be int')
        else:
            summ += num
    return summ
e = add_all_nums(1,2,3,4,5)
print(e)

def convert_celsius_to_fahrenheit(celsius):
    temp = celsius * 9/5 + 32
    return temp
f = (convert_celsius_to_fahrenheit(22))
print(f)

def check_season(month):
    Autumn = ['september','october','november']
    Winter = ['december','january','february']
    Spring = ['march','april','may']
    Summer = ['june','july','august']
    month = month.lower()
    if month in Autumn:
        season = 'Autumn'
    elif month in Summer:
        season = 'Summer'
    elif month in Spring:
        season = 'Spring'
    elif month in Winter:
        season = 'Winter'
    else:
        print('Error')
    return season
g = check_season('August')
print(g)

def solve_quadratic_eqn(a,b,c):
    dr = b^2-4*a*c
    if dr > 0:
        x1 = (-b + dr**(0.5))/2*a
        x2 = (-b - dr**(0.5))/2*a
        return x1, x2
    elif dr == 0:
        x1 = -b / 2*a
        return x1
    else:
        x1 = 'Ne imeet korney'
        return x1
    
h = solve_quadratic_eqn(1,-10,30)
print(h)

def capitalize_list_items(lst):
    rs = list()
    for i in lst:
        if isinstance(i,str):
            rs.append(i.title())
    return rs
j = capitalize_list_items(['les','pole','reka'])
print(j)

def add_item(lst,item):
    lst.append(item)
    return lst
k = add_item(['hren','s','gory'],15)
print(k)

def evens_and_odds(cif):
    a = 0
    b = 0
    for i in range(0,cif):
        if i % 2 == 0:
            a+=1
        else:
            b+=1
    return a,b
l = evens_and_odds(100)
print(l)

def factorial(a):
    fc = 1
    if a == 0:
        fc = 1
    else:
        for i in range (1,a+1):
            fc = fc * i
    return fc
m = factorial(5)
print(m)

input = list('123')
def is_empty(input):
    if len(input) == 0:
        result =  'Object is empty'  
    else:
        result =  'Object is not empty'
    return result
print(input)
n = is_empty(input)
print(n)