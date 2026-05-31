# Proyecto Integrador: Sistema de Veterinaria

Mini-sistema creado en Python para cumplir con los requisitos de POO de la sesión de hoy. Sirve para gestionar y registrar mascotas en una clínica veterinaria de forma sencilla.

## ¿Qué incluye el proyecto?
* **Clase Padre e Hijas:** `Mascota` como base, y `Perro` y `Gato` que heredan de ella.
* **Polimorfismo:** Cada animal responde con su propio sonido mediante *override*.
* **Encapsulamiento:** Lista de pacientes guardada de forma privada (`__pacientes`).
* **Métodos Especiales:** Uso de `__str__` y `__repr__` para que los datos se impriman de forma limpia.

## Estructura
El código está separado de forma organizada en: `mascota.py`, `perro_gato.py` y `clinica.py`.
