from random import randint

def twoDices():
  return randint(1,6)+randint(1,6)

frecuencies = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
expected = {2:2.78, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67, 8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}

numOfRolls = 1000

for _ in range(0,numOfRolls):
  roll = twoDices()
  frecuencies[roll] += 1
  
print("Total\tSimulated\tExpected")
print("\t  Percent\t Percent")

for dice in frecuencies:
  print("{:5d}\t{:9.2f}\t{:8.2f}".format(dice, frecuencies[dice]/numOfRolls*100, expected[dice]))