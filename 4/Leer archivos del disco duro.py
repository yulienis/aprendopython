#texto = open("Hola.txt")
#texto = open("documentos/Hola.txt")
#texto = open("../Hola.txt")
#texto = open("../doc/Hola.txt")
#print(texto.read())

#agenda = open("agendatelefonica.txt",'w')
agenda = open("agendatelefonica.txt",'a')

#agenda.truncate()
nombre = input("Introdusca su nombre: ")
telefono = input("Introdusca su numero de telefono: ")
print("Se ha guardado en la agenda el contacto: ",nombre,"con el numero de telefono: ",telefono,)

agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write(",")
agenda.write("\n")
agenda.close()
#ejerc = open("Documentos/prueba.txt")
#print(ejerc.read())

