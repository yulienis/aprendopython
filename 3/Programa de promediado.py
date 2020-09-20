nombre1 = input("dime el nombre del primer usuario ")
edad1 = input("dime la edad del primer usuario ")

nombre2 = input("dime el nombre del segundo usuario ")
edad2 = input("dime la edad del segundo usuario ")

nombre3 = input("dime el nombre del tercer usuario ")
edad3 = input("dime la edad del tercer usuario ")

print("NOMBRE \t\t EDAD ")
print(nombre1, "\t\t",  edad1)
print(nombre2, "\t\t",  edad2)
print(nombre3, "\t\t",  edad3)
edad1b = int(edad1)
edad2b = int (edad2)
edad3b = int (edad3)
suma = edad1b + edad2b + edad3b
promedio = suma/3

print("y el promedio de las edades de los usuarios es:", promedio )
