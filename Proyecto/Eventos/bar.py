
from Eventos.evento import Evento
import random



class Bar(Evento):
    def __init__(self, type_of_ticket=None, price=None, capacity=None, status=None, artist=None, event_name=None, event_date=None, opening_time=None, start_time=None, event_location=None, address=None, city=None, occupied_slots=0, tickets_sold=0, event_id=None):
        super().__init__()
        
        self.type_of_ticket = type_of_ticket
        self.price = price
        self.max_capacity = capacity
        self.event_status = status
        self.artist = artist
        self.event_name = event_name
        self.event_date = event_date
        self.opening_time = opening_time
        self.start_time = start_time
        self.event_location = event_location
        self.address = address
        self.city = city
        self.occupied_slots = occupied_slots
        self.tickets_sold = tickets_sold
        self.event_id = event_id
        self.proffit = 0.0
       

    # Event data configuration functions
    def update_data(self, type_of_ticket, price, capacity, status, artist, event_name, event_date, opening_time, start_time, event_location, address, city):
        
        self.type_of_ticket = type_of_ticket
        self.price = price
        self.max_capacity = capacity
        self.event_status = status
        self.artist = artist
        self.event_name = event_name
        self.event_date = event_date
        self.opening_time = opening_time
        self.start_time = start_time
        self.event_location = event_location
        self.address = address
        self.city = city

    


    # Functions to get event information
    def get_bar_id(self):
        return self._bar_id

    def show_state(self): #Muestra el estado del evento
        return self.event_status

    def artist_name(self): #Muestra el nombre del artista
        return self.artist

    def show_name(self): #Muestra el nombre del evento
        return self.event_name

    def show_date(self): #Muestra la fecha del evento
        return self.event_date

    def show_aperture(self): #Muestra la hora de apertura
        return self.opening_time

    def show_time(self): #Muestra la hora de inicio
        return self.start_time

    def show_location(self): #Muestra la ubicación del evento
        return self.event_location

    def show_address(self): #Muestra la dirección del evento
        return self.address

    def show_city(self): #Muestra la ciudad del evento
        return self.city

    def show_type_of_ticket(self): #Muestra el tipo de ticket
        return self.type_of_ticket 

    def show_event_id(self): #Muestra el id del evento
        return self.event_id

    def event_price(self): #Muestra el precio del evento
        return self.price

    def event_capacity(self): #Muestra la capacidad del evento
        return self.max_capacity

    def show_tickets_sold(self): #Muestra los tickets vendidos
        
        return self.tickets_sold 
    
    def add_ticket_sold(self): #Añade un ticket vendido
        self.tickets_sold += 1
        
    
    def show_slots(self): #Muestra los slots ocupados
        avaible_slots = self.event_capacity() - self.get_occupied_slots()
        return avaible_slots
    
    
    def get_proffit(self): #Obtiene el proffit
        return self.proffit

    def get_occupied_slots(self): #Obtiene los slots ocupados
        return self.occupied_slots
    
    def add_ticket_sold(self): #Agrega un ticket vendido
        self.tickets_sold += 1
    
    def assign_slot_to_client(self): #Asigna un slot a un cliente
        
        if self.get_occupied_slots() < self.event_capacity():
            self.occupied_slots += 1
            
    def add_proffit(self): #Añade el proffit
        self.proffit += self.total_commision()

    
    def total_commision(self): #Calcula la comisión total
        commision = self.event_price() * 0.8
        return commision
        
    
    def number_to_id(self):
        number = str(random.randint(0, 10000))
        return number
    