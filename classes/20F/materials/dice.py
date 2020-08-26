import random

diceRolls = ["x,y,z\n"]

for i in range(1,100):
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = x + y
    rollString = str(x) + "," + str(y) + "," + str(z) + "\n"
    diceRolls.append(rollString)

MyFile=open('dice.csv','w')
MyFile.writelines(diceRolls)
MyFile.close()
    
