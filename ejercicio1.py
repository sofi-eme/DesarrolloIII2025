class Vehiculo:
    def __init__(self, marca, modelo, patente, kilometraje):
        self.marca= marca("ingrese la marca del vehículo")
        self.modelo= modelo("ingrese el modelo del vehículo")
        self.patente= patente("ingrese la patente del mismo")
        self.kilometraje= kilometraje("ingrese el kilometraje")
    def mostrarDatos(self):
        return(f"Marca: {self.marca}, Modelo{self.modelo}, Patente:{self.patente}, Kilometraje:{self.kilometraje}")
    