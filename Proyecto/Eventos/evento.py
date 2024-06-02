from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self):
 
        self.event_status = ""         # Estado del evento
        self.artist = ""               # Nombre del artista
        self.event_name = ""           # Nombre del evento
        self.event_date = ""           # Fecha
        self.opening_time = ""         # Hora de apertura
        self.start_time = ""           # Hora de inicio
        self.event_location = ""       # Lugar
        self.address = ""              # Dirección
        self.city = ""                 # Ciudad
        self.type_of_ticket = ""       # Tipo de ticket (regular o preventa)
        self.event_id = ""             # ID del evento
        self.occupied_slots = 0         # Espacios ocupados
        self.price = 0.0               # Precio del evento
        self.max_capacity = 0           # Capacidad máxima
        self.tickets_sold = 0           # Número de tickets vendidos
        self.comission = 0.0           # Comisión por venta
        self.proffit = 0.0             # Ganancia total

    @abstractmethod
    def update_data(self, type_of_ticket, price, aforo, status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, occupied_slots, tickets_sold, event_id):
        pass
    #Sirve para asignar los valores a los atributos de la clase

    @abstractmethod
    def show_state(self): #Obtiene el estado del evento
        pass

    @abstractmethod
    def artist_name(self): #Obtiene el nombre del artista
        pass

    @abstractmethod
    def show_name(self): #Obtiene el nombre del evento
        pass

    @abstractmethod
    def show_date(self): #Obtiene la fecha del evento
        pass

    @abstractmethod
    def show_aperture(self): #Obtiene la hora de apertura
        pass 

    @abstractmethod
    def show_time(self): #Obtiene la hora de inicio
        pass

    @abstractmethod
    def show_location(self): #Obtiene el lugar del evento
        pass

    @abstractmethod
    def show_address(self): #Obtiene la dirección del evento
        pass

    @abstractmethod
    def show_city(self): #Obtiene la ciudad del evento
        pass

    @abstractmethod
    def show_type_of_ticket(self): #Obtiene el tipo de ticket
        pass

    @abstractmethod
    def show_event_id(self): #Obtiene el ID del evento
        pass

    @abstractmethod
    def event_price(self): #Obtiene el precio del evento
        pass

    @abstractmethod
    def event_capacity(self): #Obtiene la capacidad del evento
        pass

    @abstractmethod
    def show_slots(self): #Obtiene los espacios ocupados
        pass

    @abstractmethod
    def show_tickets_sold(self): #Obtiene el número de tickets vendidos
        pass

    @abstractmethod
    def total_commision(self): #Obtiene la comisión total
        pass
    
    @abstractmethod
    def add_proffit(self): #Añade la ganancia total
        pass
    
    def get_proffit(self): #Obtiene la ganancia total
        pass   
    
    def update_event(self, event_status, event_name, event_date, opening_time, start_time, event_location, address, city, type_of_ticket, price, max_capacity):
        pass
    
    @abstractmethod
    def number_to_id(self): #Convierte un número aleatorio en un ID
        pass