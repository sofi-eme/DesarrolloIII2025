#jasl
#BOM DIA BOM DIA
#anotacion
class Impresora:
    def __init__(self, marca, modelo, velocidad_ppm):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad_ppm = velocidad_ppm # Páginas por minuto
        self.__encendida = True  
        self.__cola_impresion = []

    def encender(self):
        if not self.__encendida:
            self.__encendida = True
            return "Ok, hecho. La impresora está encendida."
        return "La impresora ya estaba encendida."

    def apagar(self):
        if self.__encendida: 
            self.__encendida = False
            return "Ok, hecho. La impresora está apagada."
        return "La impresora ya estaba apagada." 

    def agregar_documento(self, documento):
        if self.__encendida:
            self.__cola_impresion.append(documento)
            return f"Documento '{documento}' agregado a la cola de impresión."
        return "La impresora está apagada. No se puede agregar documentos."

    def imprimir(self):
        if not self.__encendida: 
            return "Error: la impresora está apagada."
        if not self.__cola_impresion:
            return "No hay documentos en la cola de impresión."
        documento = self.__cola_impresion.pop(0)
        return f"Imprimiendo '{documento}' a {self.__velocidad_ppm} páginas por minuto..."

    def _str_(self):
        estado = "encendida" if self.__encendida else "apagada"
        return f"Impresora {self._marca} {self.modelo} , estado: {estado}"