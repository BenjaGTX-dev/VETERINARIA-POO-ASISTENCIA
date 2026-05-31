# Clase padre para herencia
class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return "Sonido base de animal"

    # Metodos especiales exigidos en la entrega
    def __str__(self):
        return f"{self.nombre} (Edad: {self.edad} años)"

    def __repr__(self):
        return f"Mascota('{self.nombre}', {self.edad})"