today = input('Enter today : ').lower() # the lower() function converts all inputs to lower case

print("Today is " + today)

if today == 'monday':
    print('You have class by 9am')
elif today == 'tuesday':
    print('You have a class by 1:30pm')
elif today == 'thursday':
    print('You have class by 9am')
else:
    print('no classes')
