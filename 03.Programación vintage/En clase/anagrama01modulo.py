import anagramaDict
import math

p1 = input("Una palabra: ")
p2 = input("Otra palabra: ")

if anagramaDict.isAnagram(p1, p2):
    print ("Son anagramas")
else:
    print("No son anagramas")

print("pi vale {}".format(math.pi))