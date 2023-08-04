# Day 2: 30 Days of python programming
first_name = 'Sergei'
last_name = 'Babarinov'
full_name = 'Sergei Babarinov'
country = 'Russia'
city = 'Belgorod'
age = 33
year = 2023
is_married = True
is_true = False
is_light_on = True
multi1, multi2, multi3 = '120', '130', True

type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
type(multi1)
type(multi2)
type(multi3)

len(first_name)

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = input('Radius is:')
radius = int(radius)
area_of_circle = 3.14 * radius**2
circum_of_circle = 2 * 3.14 * radius
print(area_of_circle, circum_of_circle)

# Day 3: 30 Days of python programming

age = 33
height = 179.0
comp = 1 + 12j

base = int(input('Enter base:'))
height = int(input('Enter height:'))
print('The area of the triangle is:', 0.5 * base * height)

length = int(input('Enter length:'))
width = int(input('Enter width:'))
print('The perimeter of the rectangle is:', 2 * (length + width))
print('The area of the rectangle is:', length * width)

radius = int(input('Radius is:'))
area_of_circle = 3.14 * radius**2
circum_of_circle = 2 * 3.14 * radius
print('Ares is:', area_of_circle, 'and Circumference is', circum_of_circle)

x = [-9,2,6]
y1 = 2*x[1] - 2
y2 = 2*x[2] - 2
slope = (y2 - y1)/(x[2]-x[1])
eql = ((y1 -x[1]) + (y2 - x[2])) ** 0.5
print('Slope is:', slope, 'Equlidian distance is', eql)

y = x[0]**2 + 6*x[0] + 9
print (y)

print(len('python') == len('dragon'))
print('an' in 'python' and 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'dragon' and 'python')
str(float(len('python')))

number = int(input('Give me any number:'))
print('The given number is Even:', number % 2 == 0)

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int('9.8') == 10)

hours = int(input('Enter hours:'))
rate = int(input('Enter rate per hour:'))
print('Your weekly earning is:', hour * rate)

list1 = ['Thirty','Days','of', 'Python']
print(' '.join(list1))

list1 = ['Codding','For','All']
print(' '.join(list1))

# Day 4: 30 Days of python programming

company = ('Coding For All')
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.split('Coding'))

print(company.find('Coding') != -1)
print(company.index('Coding') != None)
if "Coding" in company:
    print('True')
else: print('False')
print("Coding" in company)
print(company.replace('Coding','Python'))

print(company.split(' '))

print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
"Coding For All"[0]
len("Coding For All")-1
"Coding For All"[10]
"Coding For All"[::-1]
"Python For Everyone"[::-1]

"Coding For All".index('C')
"Coding For All".index('F')
"Coding For All People".rfind('l')
'You cannot end a sentence with because because because is a conjunction'.index('because')
'You cannot end a sentence with because because because is a conjunction'.rfind('because')
"".join('You cannot end a sentence with because because because is a conjunction'.split('because because because'))
'You cannot end a sentence with because because because is a conjunction'.find('because')
"  Coding For All   ".strip()

"# ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])
print('I am enjoying this challenge.\n I just wonder what is next')
print('Name\tAge\tCountry\tCity\nSergei\t250\tRussia\tBelgorod')


# Day 5: 30 Days of python programming

fruits = ['banana','orange','mango','lemon']

lst = list()
lst = list('stas','andrey','mikhail','sergei','anton','kostik')
first_item = lst[0]
print(first_item)
middle_item = lst[(len(lst)//2)-1]
print(middle_item)
last_item = lst[-1]
print(last_item)

mixed_data_types = ['Sergei',33,179.0,'married','Belgorod, Gubkina 43a']
it_companies = ['Facebook', 'Google','Microsoft', 'Apple','IBM','Oracle','Amazon']
print(mixed_data_types)
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[(len(it_companies)//2)-1],it_companies[-1])
it_companies[0] = 'Meta'
print(it_companies)
it_companies.append('Yandex')
print(it_companies)
it_companies.insert(((len(it_companies)//2)-1),'Cisco')
it_companies[0].upper()
print(it_companies)

preq = ['#; ']
it_companies = preq + it_companies
print(it_companies)

it_companies.index('Meta')

print(it_companies.sort())
it_companies.sort(reverse=True)

print(it_companies[0:3])
print(it_companies[-1:3])
print(it_companies[(len(it_companies)//2)-1])

del it_companies[0]
print(it_companies)
del it_companies[-1]
print(it_companies)
del it_companies[0:]
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

lst = ['Python','SQL']
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') +1, lst[0])
full_stack.insert(full_stack.index('Redux') +2, lst[1])
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print(sum(ages))
average = sum(ages)/len(ages)
print(average)
range = max_age - min_age
print(range)
print(abs(min_age - average) > abs(max_age - average))


# Day 6: 30 Days of python programming
tpl = tuple()
sisters = ('Anna', 'Adelina')
brothers = ('Viktor','Andrew')
siblings = sisters + brothers
print(siblings)
print(len(siblings))
family_members = list(siblings)
family_members.append('Natalya')
family_members.append('Leonid')
print(family_members)
parents = family_members[-2:]
siblings = family_members[:-2]
print(parents)
print(siblings)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"Estonia" in nordic_countries
"Iceland" in nordic_countries

# Day 7: 30 Days of python programming
st = set()
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Cisco','Huawei'])
print(it_companies)
it_companies.remove('Twitter')
it_companies.discard('IBM')
#Does not rise an error if object is not exist

C = A.union(B)
print(C)
print(A.intersection(B))
A.issubset(B)
A.isdisjoint(B)
A.symmetric_difference(B)
del A
del B

age = set(age)
string = 'I am a teacher and I love to inspire and teach people.'
splitset = string.split()
print(splitset)
del str_set
str_set = set(splitset)
print('Unique words count:',len(str_set))

# Day 8: 30 Days of python programming
dog = dict()
dog = {'name': 'Sobaka','color':'krasny','breed':'Ubivaka-007','legs':4,'age':1}
student = {
    'first_name': "Andrew",
    'last_name': "Sleptsov",
    'gender': "male",
    'marital status': "married",
    'skills': ['Python','Eblya Gusei','Korochanec'],
    'country': 'Russia',
    'city': 'Korocha',
    'address': {"Lugovaya st.","household 666"}
}
print(len(student)) 
student.get('skills')
type(student.get('skills'))
skills = student.get('skills')
skills.append('Hrenpoimiwo')
skills.append('Programmirovanye')
print(skills)
student['skills'] = skills
print(student)

keys = student.keys()
values = student.values()
student.pop("martiaul status")
print(student)

# Day 9: 30 Days of python programming

a = 0
if a > 0:
    print('A is a positive')
elif a <0:
    print('A is a negative')
else:
    print('A is a zero')

pills = ['blue','orange','yellow']
print ('Matrix has you') if 'blue' in pills else print ('Matrix has not have you yet')

age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print('You are able to drive')
else:
    print('You are too young to drive')

age = input('Enter your age: ')
age = int(age)
reference = 33
if age > reference:
    diff = age - reference
    print('You are older than me on {} years'.format(diff))
elif age < reference:
    diff = reference - age
    print('I am older than you on {} years'.format(diff))
else:
    print('We are the same age')

a = input('Enter your number A: ')
b = input('Enter your number B: ')
a = int(a)
b = int(b)
if a > b:
    print(a, 'is greater than', b)
elif a < b:
    print(a, 'is smaller than', b)
else:
    print('A and B the same')


score = input("Give me your score: ")
score = int(score)
if score >= 80 and score <= 100:
    print('Your grade is A')
elif score >= 70 and score <= 79:
    print('Your grade is B')
elif score >= 60 and score <= 69:
    print('Your grade is C')
elif score >= 50 and score <= 59:
    print('Your grade is D')
elif score >= 0 and score <= 49:
    print('Your grade is F')
else:
    print('Invalid score')

Autumn = ['september','october','november']
Winter = ['december','january','february']
Spring = ['march','april','may']
Summer = ['june','july','august']
month = input("Enter the month: ")
month = month.lower()
if month in Autumn:
    print('{} in Autumn'.format(month))
elif month in Summer:
    print('{} in Summer'.format(month))
elif month in Spring:
    print('{} in Spring'.format(month))
elif month in Winter:
    print('{} in Winter'.format(month))
else:
    print('Error')

fruits = ['banana','orange','mango','lemon']
new_fruit = input('Enter the fruit name: ')
if new_fruit in fruits:
    print('Fruit is already exists in list:',fruits)
else:
    fruits.append(new_fruit)
    print('New fruit would be added in', fruits)

person={
    'first_name': 'Sergei',
    'last_name': 'Babarinov',
    'age': 34,
    'country': 'Russia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '308036'
    }
    }

if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
else:
    print('There is no skills')

if 'skills' in person:
    if 'Python' in person['skills']:
        print('Person has a Python skill')
    else:
        print('Person does not have a Python skill')
else:
    print('There is no skills')

if 'skills' in person:
    skills = set(person['skills']) 
    fullstack = {'Python', 'MongoDB', 'Node', "JavaScrypt", "React"}
    frontend = {"JavaScrypt", "React"}
    backend = {'Python', 'MongoDB', 'Node'}
    if skills.intersection(frontend):
        print('Person is a frontend')
    elif skills.intersection(backend):
        print('Person is a backend')
    elif skills.intersection(fullstack):
        print('Person is a fullstack')
    else:
        print('unknown title')
else:
    print('There is no skills')

# Day 10: 30 Days of python programming

number = 0
while number <= 10:
    number +=1
    print(number)

for i in range (1,11):
    print(i)

number = 10
while number != 0:
    number = number - 1
    print(number)

for i in range (10,0,-1):
    print(i)

lst = '#######'
number = 0
while number < 7:
    number +=1
    print(lst[0:number])

print('\n'.join([i*'#' for i in range(1,8)]))

for x in range(0,8,1):
    print('')
    for t in range(0,8,1):
        print('# ', end='')
print('')
string = ''
for x in range (0,8):
    string += '# '
for i in range (0,8):
    print(string)

for x in range(0,10):
        print(x,' x ',x, ' = ', x*x)

list = ['Python', 'Numpy','Pandas','Django', 'Flask']
i = len(list)
for i in list:
    print(list[i])

for i in range(0,100,1):
    if i % 2 == 0:
        print(i)

for i in range(0,100,1):
    if i % 2 != 0:
        print(i)

for i in range(0,101,1):
    summ +=i
    print(summ) 

    a=0
b=0
for i in range(0,101,1):
    if i % 2 == 0:
        a+=i
    else:
        b+=i

print("Evenes sum: ", a)
print('Odds sum: ', b)

from countries import countries
i = 0
for i in range(1,len(countries)):
    if countries[i].find('land') != -1:
        print(countries[i])

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits1 = list()
i = 0
for i in range(len(fruits)-1,-1,-1):
     fruits1.append(fruits[i])
print(fruits1)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits2 = []
i = len(fruits)-1
while i >= 0:
    fruits2.append(fruits[i])
    i-=1

def add_two_numbers(a,b)
    summ = a + B
    return summ