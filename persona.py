class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=nombre
        self.edad=edad
def saludar (self):
    return ("hola mi nombre es {self.nombre}")

ana=persona("ana","lopez",18)
juan=persona("juan","rosales",25)

ana.saludar()
juan.saludar()

