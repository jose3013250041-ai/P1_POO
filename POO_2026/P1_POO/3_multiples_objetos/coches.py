#Multiples ojetos
class Coches:
    marca = ""
    color = "Sin color"
    velocidad = 0
    potencia = 0
    asientos = 0

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

coche1 = Coches()
coche2 = Coches()

print(f"El color del coche 1 es: {coche1.color}")
coche1.color = "Rojo y blanco"
print(f"El color del coche 1 es: {coche1.color}")
coche2.color = "Blanco y negro"
print(f"El color del coche 2 es: {coche2.color}")

print(f"La velocidad final del coche es: {coche1.velocidad}")
for i in range(1,11):
    coche1.acelerar()
print(f"La velocidad final del coche es: {coche1.velocidad}")