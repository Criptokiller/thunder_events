import streamlit as st

from Eventos.cliente import Cliente
from Gestores_de_eventos import generar_boleta
from Gestores_de_eventos.gestor_eventos import Gestor_Eventos


class Boleteria:
    def __init__(self):
        if "tickets" not in st.session_state:
            st.session_state["tickets"] = []
        if "clients" not in st.session_state:
            st.session_state["clients"] = []
        
        
        self.tickets = st.session_state["tickets"]
        self.clients = st.session_state["clients"]

        self.client = ""
        self.client_id = ""
        self.type_of_event = ""
        self.event_id = ""
        self.type_of_ticket = ""
        self.payment_method = ""
        self.attendance = None
        
    #Función para establecer los datos del ticket
    def set_data(self, client, client_id, type_of_event, event_id, type_of_ticket, payment_method):
        
        self.client = client
        self.client_id = client_id
        self.type_of_event = type_of_event
        self.event_id = event_id
        self.type_of_ticket = type_of_ticket
        self.payment_method = payment_method
        self.attendance = False
        
        
        return self #Se retorna un obejto de tipo Boleteria (el ticket)
        
    #Recibe los datos que necesita el ticket para despues añadirlo a la lista
    def add_ticket(self, client, client_id, type_of_event , event_id ,type_of_ticket, payment_method):
        
        ticket = self.set_data(client, client_id, type_of_event, event_id, type_of_ticket, payment_method)
        self.tickets.append(ticket)
        st.session_state["tickets"] = self.tickets
        
    #Añade un cliente a la lista de clientes
    def add_client(self,client):
        self.clients.append(client)
        st.session_state["clients"] = self.clients
        
    def get_client(self): #Obtiene el cliente
        return self.client
    
    def get_client_id(self): #Obtiene el id del cliente
        return self.client_id

    def get_type_of_event(self): #Obtiene el tipo de evento
        return self.type_of_event
    
    def get_event_id(self): #Obtiene el id del evento
        return self.event_id
    
    def get_type_of_ticket(self):  #Obtiene el tipo de ticket   
        return self.type_of_ticket
    
    def get_payment_method(self): #Obtiene el metodo de pago
        return self.payment_method

    def get_attendance(self): #Obtiene la asistencia (si asistio o no al evento)
        return self.attendance
    
    def get_client_data(self, client_id):
        found = False
        for client in self.clients:
            if client.get_user_id() == client_id: #Se busca el cliente por su id
                found = True
        if not found:
            st.error("Client not found")
        if found:
            return client        
        
            
    def register_attendance(self, client_id):
        found = False
        for ticket in self.tickets:
            if ticket.get_event_id() == client_id: #Se busca el ticket por el id del evento para registar la asistencia
                ticket.attendance = True
                found = True
                
        return found

    def get_tickets(self): #Obtiene todos los tickets (la lista)
        return self.tickets
    
    def get_clients_list(self):#Obtiene la lista de clientes
        return self.clients
    
    def create_pdf(self, client_id): #Función que se encarga de crear el pdf, en base al id del cliente
        events_instance = Gestor_Eventos() 
        boleteria_instance = Boleteria()
        tickets = self.get_tickets()
        generar_boleta.generate_ticket_pdf(boleteria_instance, tickets, client_id, events_instance)
        #Pasa por parametro las instancias de los gestores y la lista de tickets para crear el pdf, junto con la lista de los tickets
        #Esto para poder obtener los valores de los tickets y añadirlos al pdf
        
            
                
        
        