"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado

# def area_rectagulo (base, altura):
#     return base * altura

# print (area_rectagulo(5, 3))


#Implementar el paradigma Orientado a Objetos (OO)

class Rectagulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

rect = Rectagulo(5, 3)
print(rect.area())

# 2.-Implementar el paradigma Orientado a Objetos (OO)

class Rectagulo:
    def area(self, base, altura):
        areaR=base * altura
        return areaR

rectangulo1=Rectagulo()
# Crear o instanciar un objeto "rectangulo1" de la clase "Rectagulos"
print(f"El area del rectangulo es: {rectangulo1.area(5, 6)}")