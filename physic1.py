print('welcome pls choose your desired formula')
print('a- force\nb-electrical power\nc-velocity\nd-voltage\ne-potential energy')
k = input('what is your desired formula')
if k =='a':
 print('u have chosen force')
 mass=float(input('enter your desired mass'))
 acceleration = float(input('enter your desired acceleration'))
 print(mass * acceleration)
 if k == 'b':
     print('you have chosen electrical power')
     voltage = float(input('enter your desired voltage'))
     current = float(input('enter your desired current'))
     print(voltage * current)

if k == 'c':
    print('you have chosen velocity')
    displacement = float(input('enter your desired displacement'))
    time = float(input('enter your desired time'))
    print(displacement / time)

if k == 'd':
    print('you have chosen voltage')
    current = float(input('enter your desired current'))
    resistance = float(input('enter your desired resistance'))
    print(resistance * current)

if k == 'e':
    print('you have chosen potential energy')
    mass = float(input('enter your desired mass'))
    acc_due_to_gravity= float(input('enter your desired acc_due_to_gravity'))
    height = float(input('enter your desired height'))
    print(mass * height * acc_due_to_gravity)
else:
    print('please pick among the available formulae')
