# PRÁCTICA 2 --> EJERCICIO 2
# Convertir de grados centígrados a grados Fahrenheit.

print("Bienvenido a la calculadora de grados centígrados a grados Fahrenheit")
print("Ponga los Grados centígrados que quiera convertir:")
centigrados = float(input())
print("Ha puesto:", centigrados, "grados")
fahrenheit = float((centigrados * 9/5) + 32)
print("Que son", fahrenheit, "grados Fahrenheit")