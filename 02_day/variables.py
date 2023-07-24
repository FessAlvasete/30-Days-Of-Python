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

company = ('Codding For All')
print(company)