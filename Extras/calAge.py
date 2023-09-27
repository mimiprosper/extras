
#DoB = int(input('Enter you DoB: '))
#age = str(2022 - DoB)
#print('You are ' + age + 'yrs old')


#error handling
try:
    DoB = int(input('Enter you DoB: '))
    age = 2022 - DoB
    #print('You are', age, 'yrs old') 
    print(f'You are {age} yrs old')  #string formatting
except ValueError:
    print('you have entered an invalid input')
except:
    print('there was an error, try again')

   