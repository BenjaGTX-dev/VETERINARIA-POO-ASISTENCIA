from perro_gato import Perro, Gato

class Veterinaria:
    def __init__(self, nombre_clinica):
        self.nombre_clinica = nombre_clinica
        # Atributo privado/encapsulado con doble guion bajo
        self.__pacientes = [] 

    def agregar_paciente(self, mascota):
        # Aqui se cumple composicion (guarda objetos de otra clase)
        self.__pacientes.append(mascota)
        print(f"-> Registrado: {mascota.nombre}")

    def listar_historial(self):
        print(f"\n=== CLINICA: {self.nombre_clinica} ===")
        if not self.__pacientes:
            print("No hay animales registrados.")
            return
        
        # Polimorfismo en accion corriendo la lista mixta
        for p in self.__pacientes:
            print(f"Paciente: {p} | Ruido: {p.hacer_sonido()}")

# Script de prueba para ejecutar en la terminal de VS Code
if __name__ == "__main__":
    control = Veterinaria("Pet Care San Pablo")

    p1 = Perro("Firulais", 4, "Pitbull")
    g1 = Gato("Michi", 2, es_arisco=False)

    print("--- Test de __str__ y __repr__ ---")
    print(str(p1))
    print(repr(g1))
    print("---------------------------------\n")

    control.agregar_paciente(p1)
    control.agregar_paciente(g1)

    control.listar_historial()