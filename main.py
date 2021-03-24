#following Udemy course: 100 days of code by Angela Yu

number = int(input ('Please enter an intger?\n'))
x=number%2
if x==0:
    print ('that is an even nunber')
else: 
    print ('that is an odd number')
print(x)

#-----------------------------------

print ('\n\n-------WELCOME TO THE BMI CALCULATOR-------')
weight = float(input ('enter the weight in kg?\n'))
height = float(input ('enter the height in m\n'))
wholeBMI = weight / (height * height)
BMI = round(wholeBMI)
print(BMI)

if BMI <= 18.5:
    print('You are UNDERweight')
elif BMI <= 25:
    print('You are NORMAL weight')
elif BMI <= 30:
    print('You are slightly OVERweight')
elif BMI <= 35:
    print('You are OBESE')
else:
    print('You are clinically OBESE')

    
    
#----------------------------
#https://ascii.co.uk/art
print('''
              _         _
  __   ___.--'_`.     .'_`--.___   __
 ( _`.'. -   'o` )   ( 'o`   - .`.'_ )
 _\.'_'      _.-'     `-._      `_`./_
( \`. )    //\`         '/\\    ( .'/ )
 \_`-'`---'\\__,       ,__//`---'`-'_/
  \`        `-\         /-'        '/
   `                               '  
''')
print('\n\n---------------We can tell you if entered year is a leap or normal---------------')

year = int(input ('Please enter the year?\n'))

if year % 4 == 0:
    #print ('LEAP')

    if year % 100 == 0:
        #print ('NORMAL')

        if year % 400 == 0:
            print ('LEAP')
        else: 
            print ('NORMAL')

    else: 
        print ('LEAP')

else: 
    print ('NORMAL')

    
#----------------------------
size = input ('Please pick a size for your pizza: S, M, L\n')
if size == 'S':
    total = 15
elif size == 'M':
    total = 20
else:
    total = 25

pepperoni = input ('Do you want pepperony: Y or N\n')

if pepperoni == 'Y':
    if size == 'S':
        total += 2
    else:
        total += 3
else:
    pass

extra_cheese = input ('Do you want extra cheese: Y or N\n')

if extra_cheese == 'Y':
    total += 1
print(total)

#----------------------------
#kids name macthing game
name1=input("First name: ")
name2=input("Second name: ")
name=name1.lower()+name2.lower()

result1 = 0
for x in name:
    if x in "true":
        result1 += 1
    else: 
        pass

result2 = 0
for x in name:
    if x in "love":
        result2 += 1
    else: 
        pass

#print(f'Your score is: {result1}{result2}')

#change int into str
result1=str(result1)
result2=str(result2)
result =result1+result2
#change back to int
result = int(result)

if result < 10 or result > 90:
    print (f'Your score is {result}, you go together like coke and mentos')
elif result > 40 and result < 50:
    print (f'Your score is {result}, you are alright together')
else:
    print (f'Your score is {result}')
