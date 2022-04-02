#SOLUCIÓN
strPeople = input("¿Cuantas personas? ")
strPizzas = input("¿Cuantas pizzas? ")

people = int(strPeople)
pizzas = int(strPizzas)

if people % 2 == 1:
  porciones = people + 1
else:
  porciones = people
  
print("{} personas toman {} pizzas".format(people, pizzas))
print("Cada persona toma {} porciones".format(pizzas))
print("Sobran {} porciones".format((porciones * pizzas) % people))