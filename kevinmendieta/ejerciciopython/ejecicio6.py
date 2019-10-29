"""
  @autor: kevin
  nombre: ejecicio5.py
  descripcion: ...

  Kevin.Mendieta.--.19
  ---Su.suma.de.notas.es:.19
  ---Su.promedio.es:.15
"""
 

nombre = input("Ingrese su nombre:")
edad = input("Ingrese su edad: \n")
nota1= input("Ingrese el valor de su nota 1: ")
nota2 =input ("Ingresa el valor de su nota 2: ")

suma = int(nota1) * int(nota2);
print("%s -- %s\nSu suma de notas es %s" %
	(nombre, edad, suma))