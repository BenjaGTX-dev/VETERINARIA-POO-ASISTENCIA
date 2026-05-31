from mascota import Mascota

# Herencia y override de metodos
class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Uso de super() obligatorio
        self.raza = raza

    def hacer_sonido(self):  # Override
        return "Guau!"

class Gato(Mascota):
    def __init__(self, nombre, edad, es_arisco=True):
        super().__init__(nombre, edad)
        self.es_arisco = es_arisco

    def hacer_sonido(self):  # Override
        return "Miau!"