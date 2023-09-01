from math import floor
base = 230
stat_lv99 = 5200
#currentLevel = int(input('Current user level (shulk): '))

stat = []

for i in range(99):
    currentLevel = i+2
    
    base = floor((floor(((stat_lv99 - base) * 120) / (120 - (currentLevel))) + 25) / 50) + base
    print("Lvl: " + str(currentLevel) + " - " + str(base) + "\n")
    
    #print(currentLevel)
    
    #if currentLevel == 2:
    #    print("Lvl: " + str(currentLevel) + " - " + str(base) + "\n")
        
    #if currentLevel == 99:
    #    print("Lvl: " + str(currentLevel) + " - " + str(base) + "\n")
    
