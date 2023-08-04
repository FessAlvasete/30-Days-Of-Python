fruits = ['banana','orange','mango','lemon']
new_fruit = input('Enter the fruit name: ')
if new_fruit in fruits:
    print('Fruit is already exists in list:',fruits)
else:
    fruits.append(new_fruit)
    print('New fruit would be added in', fruits)