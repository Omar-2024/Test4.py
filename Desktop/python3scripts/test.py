import numpy as np

user_input = input('Please insert how many values for 1-10: ')


# range(1,10,10) is the same
for i in np.linspace(1,10,int(user_input)):
    print(i)
print('\nMission COMPLETE. Printed out ' + user_input + ' values')
