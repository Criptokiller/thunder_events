import random
from Eventos.evento import Evento 



class Filantropico(Evento):
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
       
    # Funciones de configuración de datos del evento
    def update_data(self, type_of_ticket, price, capacity, status, artist, event_name, event_date, openingTime, start_time, event_location, address, city):
        
        self.type_of_ticket = type_of_ticket
        self.price = price
        self.max_capacity = capacity
        self.event_status = status
        self.artist = artist
        self.event_name = event_name
        self.event_date = event_date
        self.opening_time = openingTime
        self.start_time = start_time
        self.event_location = event_location
        self.address = address
        self.city = city
    
    
    
    def set_stats(self):
        self.event_id = self.number_to_id()


    def show_state(self):
        return self.event_status

    def artist_name(self):
        return self.artist

    def show_name(self):
        return self.event_name

    def show_date(self):
        return self.event_date

    def show_aperture(self):
        return self.opening_time

    def show_time(self):
        return self.start_time

    def show_location(self):
        return self.event_location

    def show_address(self):
        return self.address

    def show_city(self):
        return self.city

    def show_type_of_ticket(self):
        return self.type_of_ticket

    def show_event_id(self):
        return self.event_id

    def event_price(self):
        return self.price

    def event_capacity(self):
        return self.max_capacity

    def show_tickets_sold(self):

        return self.tickets_sold
    
    
    def number_to_id(self):
        number = str(random.randint(0, 10000))
        return number

    def show_slots(self): #Cantidad de slots disponibles
        avaible_slots = self.event_capacity() - self.get_occupied_slots()
        return avaible_slots
    
    def add_proffit(self):
        self.proffit += self.total_commision()
    
    def get_proffit(self):
        return self.proffit
    
    
    def assign_slot_to_client(self):
        if self.get_occupied_slots() < self.event_capacity():
            self.occupied_slots += 1
    
    def add_ticket_sold(self): #Agrega un ticket vendido
        self.tickets_sold += 1
            


    def get_occupied_slots(self):
        return self.occupied_slots
    
    def total_commision(self):
        commission = self.price
        return commission