"""
  @autor: kevin
  nombre: ejecicio4.py
  descripcion: ...
"""
# System.out.println("Ingrese su nombre")
# nombre = entrada.nextLine()

nombre = input("Ingrese su nombre:")
edad = input("Ingrese su edad: \n")
nota1= input("Ingrese el valor de su nota 1: ")
nota2 =input ("Ingresa el valor de su nota 2: ")

suma = nota1 + nota2;
print("%s -- %s\nSu suma de notas es %s" %
	(nombre, edad, suma))