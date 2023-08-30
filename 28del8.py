class Avion:
    def __init__(self, modeloavion, asientos):
        self.modeloavion = modeloavion
        self.asientos = asientos
   
    def __str__(self):
        return f"{self.modeloavion}"    
class vuelo:
     def __init__(self, nvuelo, origen, destino, fecha, hora, _avion ):
         self.nvuelo = nvuelo
         self.origen=origen
         self.destino= destino
         self.fecha= fecha
         self.hora=hora
         self._avion=_avion
         self.reservaciones=[]
     
     def __str__(self):
        return f"{self.nvuelo}, {self.origen}, {self.destino}, {self.fecha}, {self.hora} {self._avion}"  
    
     def reservar(self,_reserva):
        self.reservaciones.append(_reserva)
    
     def mostrar_reservas(_reserva):
        print("reservas:")
        for _reserva in vuelo_1.reservaciones:
            print(f"Su numero reserva {_reserva.nreserva} (Pasajero: {_reserva._pasajero}), (Vuelo: {_reserva._vuelo}) Estado: {_reserva.estado}")

     def eliminar_reservacion(self, nreserva):
        for reserva in self.reservaciones:
            if reserva.nreserva == nreserva:
                confirmacion = input(f"¿Estás seguro de quiere eliminar la reserva {nreserva} ? para confirma con Y y canselar la accion con N (Y/N): ")
                if confirmacion == "Y":
                    self.reservaciones.remove(reserva)
                    print(f"La reserva {nreserva} ha sido eliminada con exito")
                elif confirmacion == "N":
                    print("La eliminacion de la reserva a sido cancelada")

class Vuelos:
    def __init__(self):
        self.Vuelos = []

    def Vuelos_disponibles(self, avuelo):
        self.Vuelos.append(avuelo)


    def mostrar_vuelos(_vuelo):
        print("Vuelos disponibles:")
        for _vuelo in vuelos_1.Vuelos:
            print(f"Vuelo Disponible : --------------------- {_vuelo.nvuelo}, Lugar de Origen: {_vuelo.origen}, Lugar de Destino: {_vuelo.destino}, Fecha asignada: {_vuelo.fecha}, Hora de: {_vuelo.hora}, Avion asignado: {_vuelo._avion}"
                  "---------------------")    
class reservacion:
    def __init__(self, nreserva, _pasajero, _vuelo, estado):
        self.nreserva=nreserva
        self._pasajero=_pasajero
        self._vuelo=_vuelo
        self.estado=estado

        
vuelos_1= Vuelos()

avion_17 = Avion("bartolome 14", 60)
avion_18 = Avion("bartolome 15", 60)
avion_183 = Avion("bartolome 16", 60)
avion_184 = Avion("bartolome 17", 60)
avion_185 = Avion("bartolome 18", 60)

vuelo_1 = vuelo(1,str(input("ingrese origen ")), str(input("ingrese destino ")), str(input("ingrese fecha")), str(input("ingrese hora ")),avion_17)
vuelo_12 = vuelo(2,"santiago", "miami", "17/08/24", "17:40",avion_18)
vuelo_13 = vuelo(3,"santiago", "miami", "17/08/24", "17:40",avion_183)
vuelo_14 = vuelo(4,"miami", "peru causa", "17/08/24", "17:40",avion_184)

vuelos_1.Vuelos_disponibles(vuelo_1)
vuelos_1.Vuelos_disponibles(vuelo_12)
vuelos_1.Vuelos_disponibles(vuelo_13)
vuelos_1.Vuelos_disponibles(vuelo_14)

Vuelos.mostrar_vuelos(vuelo_1)


class Pasajero:
    def __init__(self, pasaporte, nombre):
        self.pasaporte = pasaporte
        self.nombre = nombre
        self.vuelos_reservados = []
    
    def __str__(self):
        return f"{self.pasaporte}, {self.nombre}"
    # def reservar(self,_reserva):
    #     self.vuelos_reservados.append(_reserva)
    
    # def vuelo_reservado(self):
    #     print(f"Vuelos reservados para{self.nombre} N°Pasaporte {self.pasaporte}:")

    #     for vuelo in self.vuelos_reservados:
    #         print(f"Número de vuelo: ______ {vuelo.nvuelo}, Origen:___ {vuelo.origen}, Destino: ___{vuelo.destino}, Fecha:__ {vuelo.fecha}, Hora: {vuelo.hora}")


pasajero_1 = Pasajero("AB123456", "Jose Ernandes")
pasajero_2 = Pasajero("CD789012", "Maria Canalio")
pasajero_3 = Pasajero("EF345678", "Nashe")

# pasajero_1.reservacion_vuelo(vuelo_1)
# pasajero_2.reservacion_vuelo(vuelo_12)
# pasajero_3.reservacion_vuelo(vuelo_13)
# pasajero_1.reservacion_vuelo(vuelo_14)

reserva= reservacion(1, pasajero_1, vuelo_1, "reservado")
vuelo.reservar(vuelo_1, reserva)
vuelo.mostrar_reservas(reserva)

vuelos_1.mostrar_vuelos()

numero_vuelo_mostrar_reservas = int(input("Ingrese el numero del vuelo para mostrar sus reservaciones: "))
for vuelo_actual in vuelos_1.Vuelos:
    if vuelo_actual.nvuelo == numero_vuelo_mostrar_reservas:
        vuelo_actual.mostrar_reservas()


numero_reserva_a_eliminar = int(input("Ingrese el numero de la  reserva que desea eliminar  a continuacion: "))
for vuelo_actual in vuelos_1.Vuelos:
    vuelo_actual.eliminar_reservacion(numero_reserva_a_eliminar)

vuelos_1.mostrar_vuelos()




        


